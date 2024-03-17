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

    headers = {
        "X-Client-Version": "3.4"
    }

    try:
        response = session.post(url=url, data=payload, headers=headers)
        
        json_response = response.json()
        
        # print(json_response)
        
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
    
    payload = {
    "organizationUid": "0a093973-274b-4df8-83e2-2316dee0c9a9",
    "role": "CompanySubtenant",
    "mfaPolicyStatus": "Enabled",
    "profile": {
        "firstName": "John",
        "lastName": "Brown",
        "title": "Mr.",
        "email": "j.brown@exonco.com",
        "address": "",
        "phone": "301 329 9338"
    },
    "credentials": {
        "userName": "subtenant",
        "password": "Password1"
    },
    "backupResource": {
        "siteUid": "0107365a-60f9-422a-832b-585db173d356",
        "companySiteBackupResourceUid": "886a9551-f365-4ef7-9bcc-c227bd288369",
        "description": "",
        "vcdUserId": "",
        "resourceFriendlyName": "CloudRepo",
        "storageQuota": "1073741824",
        "isStorageQuotaUnlimited": ""
    }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}",
        "X-Client-Version": "3.4"
    }

    response = session.post(url=url, data=payload, headers=headers)


    data = response.json()
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

get_companies()
