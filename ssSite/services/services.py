import time

from django.conf import settings
from requests import Session


def get_token():
    # Base:port / area
    url = "https://192.168.210.44:1280/api/v3/token"

    payload = {
        "grant_type": "password",
        "username": r"demo_zero_one\api_user",
        "password": "S1l1conSky@DEV",
    }

    headers = {"X-Client-Version": "3.4"}

    try:
        response = session.post(url=url, data=payload, headers=headers)

        json_response = response.json()

        print(json_response)

        bearer_token = json_response["access_token"]

        return bearer_token

    except Exception as ex:
        return print(ex)


def get_user():
    try:
        # Attempt to retrieve APIUser associated with the user in the request
        api_user = Sot.objects.get(user=request.user)

        # Check if the username is None
        if api_user.user.username is None:
            none_flag = True

    except APIUser.DoesNotExist:
        # APIUser not found
        none_flag = True

    except Exception as e:
        # Other unexpected errors
        none_flag = True

    if none_flag:
        # Log a message and return 404 status if no APIUser is found
        # print(f'[Not Found] No API User Found for: {request.user.username}...\n')
        return 404

    # Log success and return the APIUser object
    # print('[SUCCESS] Found API User! -- USERNAME:', api_user.user.username, end='\n')
    return api_user


def create_user(request):
    url = "https://192.168.210.44:1280/api/v3/users"

    bearer_token = get_token()

    query = {"select": '[{"propertyPath":"json"}]'}

    headers = {
        "accept": "application/json",
        "X-Request-id": "497f6eca-6276-4993-bfeb-43cbbbba6f35",
        "Authorization": f"Bearer {bearer_token}",
    }

    data = {
        "organizationUid": "3110a9da-7ea1-4857-98cb-c3e5c46b6dd6",
        "role": "CompanyTenant",
        "mfaPolicyStatus": "Disable",
        "profile": {
            "firstName": "Test",
            "lastName": "van Staden",
            "title": "Mr",
            "email": "brands@siliconsky.com",
            "address": None,
            "phone": "081 565 0206",
        },
        "credentials": {"userName": "branden_van_staden", "password": "Markaway86#"},
        "backupResource": {
            "siteUid": "b65acaf4-e282-4096-9e56-8c840442a3a3",
            "companySiteBackupResourceUid": "a2b21ca5-55cc-4616-8b39-6270c0741b26",
            "description": None,
            "vcdUserId": None,
            "resourceFriendlyName": "BCloudRepo",
            "storageQuota": 1073741824,
            "isStorageQuotaUnlimited": False,
        },
    }

    response = session.post(url=url, json=data, headers=headers, params=query)

    print(response.headers)
    print()
    print(response.status_code)

    try:
        print(response.json())
    except Exception as ex:
        print(ex)


# class SessionManager:
#     def __init__(self, request):
#         self.request = request
#         self.session = Session()

#     def get_session(self):
#         api_user = TenantUser.objects.get(user=self.request.user)

#         self.session.headers = {
#             "Content-Type": "application/json",
#             "Authorization": f"Bearer {api_user.access_token}",
#             "Accept-Encoding": "gzip",
#         }
#         return self.session

#     def get_token(self):
#         url = "https://192.168.210.44:1280/api/v3/token"

#         payload = {
#             "grant_type": "password",
#             "username": r"demo_zero_one\api_user",
#             "password": "S1l1conSky@DEV",
#         }

#         headers = {"X-Client-Version": "3.4"}

#         try:
#             response = self.session.post(url=url, data=payload, headers=headers)

#             json_response = response.json()

#             print(json_response)

#             bearer_token = json_response["access_token"]

#             return bearer_token

#         except Exception as ex:
#             return print(ex)
