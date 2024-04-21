import uuid

import requests
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import StorageAllocation


@login_required(login_url="web_application:login")
def index_1(request):
    return render(request, "storage_allocation_1.html")


def get_token():
    # Session - Provides Connection Pooling Persistence
    session = requests.Session()

    # Disable Verification
    session.verify = False

    # Prevent Tracking
    session.trust_env = False

    # Base:port / area
    url = "https://192.168.210.44:1280/api/v3/token"

    payload = {
        "grant_type": "password",
        "username": r"demo_zero_one\api_user",
        "password": "S1l1conSky@DEV",
    }

    session.headers = {"X-Client-Version": "3.4"}

    try:
        response = session.post(url, data=payload)

        json_response = response.json()
        bearer_token = json_response["access_token"]

        return bearer_token

    except Exception as ex:
        return print(ex)


@login_required(login_url="web_application:login")
def allocate_storage(request):
    # Session - Provides Connection Pooling Persistence
    session = requests.Session()

    # Disable Verification
    session.verify = False
    # Prevent Tracking
    session.trust_env = False

    if request.method == "POST":

        # Profile Detail
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        title = request.POST.get("title")
        email_address = request.POST.get("email_address")
        physical_address = request.POST.get("physical_address")
        phone_number = request.POST.get("phone_number")

        # Credential Detail
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Backup Resource Detail
        resource_name = request.POST.get("resource_name")
        resource_description = request.POST.get("resource_description")
        vcd_user_id = request.POST.get("vcd_user_id")
        storage_quota = request.POST.get("storage_quota")

        if title == 1:
            title = "Mr"
        else:
            title = "Mrs"

        obj_allocation = StorageAllocation(
            user=request.user,
            firstName=first_name,
            lastName=last_name,
            title=title,
            email=email_address,
            address=physical_address,
            phone=phone_number,
            userName=request.user.username,
            password=password,
            resourceFriendlyName=resource_name,
            description=resource_description,
            vcdUserId=vcd_user_id,
            storageQuota=storage_quota,
        )

        print(obj_allocation)
        obj_allocation.save()

        url = "https://192.168.210.44:1280/api/v3/users"

        bearer_token = get_token()

        params = {"select": '[{"propertyPath":"json"}]'}

        headers = {
            "accept": "application/json",
            "X-Request-id": str(uuid.uuid4()),
            "Authorization": f"Bearer {bearer_token}",
        }

        payload = {
            "organizationUid": str(obj_allocation.organizationUid),
            "role": "CompanySubtenant",
            "mfaPolicyStatus": "Disabled",
            "profile": {
                "firstName": str(obj_allocation.firstName),
                "lastName": str(obj_allocation.lastName),
                "title": str(obj_allocation.title),
                "email": str(obj_allocation.email),
                "address": str(obj_allocation.address),
                "phone": str(obj_allocation.phone),
            },
            "credentials": {
                "userName": str(obj_allocation.userName),
                "password": str(obj_allocation.password),
            },
            "backupResource": {
                "siteUid": str(obj_allocation.siteUid),
                "companySiteBackupResourceUid": str(
                    obj_allocation.companySiteBackupResourceUid
                ),
                "description": str(obj_allocation.description),
                "vcdUserId": str(obj_allocation.vcdUserId),
                "resourceFriendlyName": str(obj_allocation.resourceFriendlyName),
                "storageQuota": str(obj_allocation.storageQuota),
                "isStorageQuotaUnlimited": False,
            },
        }

        response = session.post(url, json=payload, headers=headers, params=params)

        output = f"""({response.status_code}) Response from {url}
        [{request.method}]
            
        Headers:
        {response.headers}
            
        Body:
        """
        print(output)

        try:
            data = response.json()
            print(data)
        except Exception as ex:
            print(ex)

        return HttpResponseRedirect(reverse("web_application:home"))
    return render(request, "storage_allocation_2.html")
