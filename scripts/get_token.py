import json

import requests

# Session - Provides Connection Pooling Persistence
session = requests.Session()

# Disable Verification
session.verify = False

# Prevent Tracking
session.trust_env = False


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


def create_company():
    # url = "https://192.168.210.44:1280/api/v3/organizations/companies"

    bearer_token = get_token()

    query = {"select": '[{"propertyPath":"json"}]'}

    headers = {
        "accept": "application/json",
        "X-Request-id": "ba547d14-c556-42bb-b85c-eeeb16e2f5e7",
        "Authorization": f"Bearer {bearer_token}",
        "x-veeam-vspc-patch-for": json.dumps(
            {
                "$ref": "https://192.168.210.44:1280/api/v3//components/schemas/CompanyPermissions"
            }
        ),
    }

    company_uid = "3110a9da-7ea1-4857-98cb-c3e5c46b6dd6"

    url = (
        "https://192.168.210.44:1280/api/v3/organizations/companies/"
        + company_uid
        + "/permissions"
    )

    payload = [
        {"op": "add", "path": "/-/demo_zero_one", "value": "REST"},
    ]

    # session.headers = headers
    # response = session.patch(url, payload)
    response = session.request(
        url=url,
        method="patch",
        data=payload,
        headers=headers,
        params=query,
        verify=False,
    )

    data = response
    print(data.headers, response.json())

    # payload = {
    #     "resellerUid": None,
    #     "organizationInput": {
    #         "name": "Test-org",
    #         "alias": "test-org",
    #         "taxId": "643-70-9745",
    #         "email": "j.doe@siliconsky.com",
    #         "phone": "906-284-7082",
    #         "country": 1,
    #         "state": 22,
    #         "countryName": "RSA",
    #         "regionName": "Western Cape",
    #         "city": "Cape Town",
    #         "street": "123 Main road, Claremont",
    #         "notes": None,
    #         "zipCode": 7001,
    #         "website": "www.bcodelabs.com",
    #         "veeamTenantId": None,
    #     },
    #     "subscriptionPlanUid": None,
    #     "permissions": ["REST"],
    #     "isAlarmDetectEnabled": False,
    #     "companyServices": {
    #         "isBackupAgentManagementEnabled": True,
    #         "isFileLevelRestoreEnabled": False,
    #         "isBackupServerManagementEnabled": True,
    #         "isVBPublicCloudManagementEnabled": True,
    #     },
    # }

    # query = {"select": '[{"propertyPath":"json"}]'}

    # response = session.post(
    #     url, headers=headers, json=payload, params=query, verify=False
    # )

    # data = response.json()
    # print(data)


def create_user():
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
        "role": "Company Owner",
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


def get_companies():
    url = "https://192.168.210.44:1280/api/v3/organizations/companies"

    bearer_token = get_token()

    print(bearer_token)

    headers = {"Authorization": f"Bearer {bearer_token}", "X-Client-Version": "3.4"}

    response = session.get(url, headers=headers)

    data = response.json()
    print(data)

    """
    {
        "meta": {
        "pagingInfo": {
            "total": 1,
            "count": 1,
            "offset": 0
        }
        },
        "data": [
        {
            "instanceUid": "3110a9da-7ea1-4857-98cb-c3e5c46b6dd6",
            "name": "Demo Zero One",
            "status": "Active",
            "resellerUid": None,
            "subscriptionPlanUid": None,
            "permissions": [
            "REST"
            ],
            "isAlarmDetectEnabled": False,
            "companyServices": {
            "isBackupAgentManagementEnabled": False,
            "isFileLevelRestoreEnabled": False,
            "isBackupServerManagementEnabled": False,
            "isVBPublicCloudManagementEnabled": False
            },
            "loginUrl": None,
            "_embedded": {
            "organization": None
            }
        }
        ]
    }
    """


def backup_servers():
    url = "https://192.168.210.44:1280/api/v3/infrastructure/backupServers"

    bearer_token = get_token()

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "X-Client-Version": "3.4",
    }

    response = session.get(url, headers=headers)

    data = response.json()
    print(data)
