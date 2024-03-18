import requests

# Session - Provides Connection Pooling Persistence
session = requests.Session() 
# Disable Verification
session.verify = False
# Prevent Tracking
session.trust_env = False

def get_token():
    url = "https://192.168.210.44:1280/api/v3/token"

    payload = {
        "grant_type": "password",
        "username": r"demo_zero_one\api_user",
        "password": "S1l1conSky@DEV",
    }

    # payload = {
    #     "grant_type": "password",
    #     "username": r"SILICONSKY\svc_veeamlab",
    #     "password": "S1l1conSky@DEV",
    # }
    
    headers = {
        "X-Client-Version": "3.4"
    }

    try:
        response = session.post(url=url, data=payload, headers=headers)
        
        json_response = response.json()
        
        print(json_response)
        
        bearer_token = json_response["access_token"]
        
        return bearer_token
    
    except Exception as ex:        
        return print(ex)

def create_company():
    url = "https://192.168.210.44:1280/api/v3/organizations/companies"

    payload = {
        "resellerUid": None,
        "organizationInput": {
            "name": "Test-org",
            "alias": "test-org",
            "taxId": "643-70-9745",
            "email": "j.doe@siliconsky.com",
            "phone": "906-284-7082",
            "country": 1,
            "state": 22,
            "countryName": "RSA",
            "regionName": "Western Cape",
            "city": "Cape Town",
            "street": "123 Main road, Claremont",
            "notes": None,
            "zipCode": 7001,
            "website": "www.bcodelabs.com",
            "veeamTenantId": None
        },
        "subscriptionPlanUid": None,
        "permissions": [
            "REST"
        ],
        "isAlarmDetectEnabled": False,
        "companyServices": {
            "isBackupAgentManagementEnabled": True,
            "isFileLevelRestoreEnabled": False,
            "isBackupServerManagementEnabled": True,
            "isVBPublicCloudManagementEnabled": True
        }
    }

    headers = {
        "Content-Type": "application/json",
        "X-Request-id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "X-Client-Version": "3.4"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)

def create_user():
    url = "https://192.168.210.44:1280/api/v3/users"

    bearer_token = get_token()
    
    query = {
  "select": "[{\"propertyPath\":\"json\"}]"
}
    payload = {
    "organizationUid": "3110a9da-7ea1-4857-98cb-c3e5c46b6dd6", # Instance Uid: /organizations/companies
    "role": "CompanySubtenant",
    "mfaPolicyStatus": "Disabled",
    "profile": {
        "firstName": "John",
        "lastName": "Brown",
        "title": "Unknown",
        "email": "brandenconnected@gmail.com",
        "address": "",
        "phone": "301 329 9338"
    },
    "credentials": {
        "userName": "testUser",
        "password": "Phil017bvsbvs123"
    },
    "backupResource": {
        "siteUid": "b65acaf4-e282-4096-9e56-8c840442a3a3", # siteUid: /organizations/companies/sites
        "companySiteBackupResourceUid": "a2b21ca5-55cc-4616-8b39-6270c0741b26", # InstanceUid: /organizations/companies/sites/backupResources
        "description": "",
        "vcdUserId": "",
        "resourceFriendlyName": "VCC-LAB",
        "storageQuota": 1073741824,
        "isStorageQuotaUnlimited": "false"
    }
    }

    headers = {

        "Authorization": f"Bearer {bearer_token}",
        "X-Client-Version": "3.4"
    }

    response = session.post(url=url, json=payload, headers=headers, params=query)


    data = response
    print(data)

def get_companies():
    url = "https://192.168.210.44:1280/api/v3/organizations/companies"

    bearer_token = get_token()
    
    print(bearer_token)

    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "X-Client-Version": "3.4"
    }

    response = session.get(url, headers=headers)

    data = response.json()
    print(data)
    
    '''
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
    '''

def backup_servers():
    url = "https://192.168.210.44:1280/api/v3/infrastructure/backupServers"


    bearer_token = get_token()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "X-Client-Version": "3.4"
    }

    response = session.get(url, headers=headers)

    data = response.json()
    print(data)

create_user()
