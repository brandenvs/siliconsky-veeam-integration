import requests, certifi, urllib3

# Setup Session
session = requests.Session()  # Provides Connection Pooling Persistence
session.verify = False  # Disable Verification
session.trust_env = False  # Prevent Tracking


def get_token():
    url = "https://192.168.210.44:1280/api/v3/token"

    payload = {
    "grant_type": "password",
    "username": r"demo_zero_one\api_user",
    "password": "D3v@VanSPython",
    "refresh_token": "",
    "mfa_token": "",
    "mfa_code": "",
    "code": "",
    "public_key": "",
    "userUid": ""
    }

    headers = {
        "X-Client-Version": "3.4"
    }

    try:
        response = session.post(url=url, data=payload, headers=headers)
        json_response = response.json()
        
        bearer_token = json_response['access_token']
        return bearer_token
    
    except Exception as ex:
        print(ex)
        return ex

def create_user():
    url = "https://192.168.210.44:1280/api/v3/users"
    
    query = {
      "select": "[{\"propertyPath\":\"string\"}]"
    }
    
    payload = {
    "organizationUid": "3110a9da-7ea1-4857-98cb-c3e5c46b6dd6",
    "role": "CompanySubtenant",
    "mfaPolicyStatus": "Enabled",
    "profile": {
        "firstName": "John",
        "lastName": "Brown",
        "title": "Mr",
        "email": "j.brown@exonco.com",
        "address": None,
        "phone": "301 329 9338"
    },
    "credentials": {
        "userName": "subtenant",
        "password": "Password1"
    },
    "backupResource": {
        "siteUid": "0107365a-60f9-422a-832b-585db173d356",
        "companySiteBackupResourceUid": "886a9551-f365-4ef7-9bcc-c227bd288369",
        "description": None,
        "vcdUserId": None,
        "resourceFriendlyName": "Lab\VCC-Exagrid",
        "storageQuota": 1073741824,
        "isStorageQuotaUnlimited": False
    }
    }

    
    bearer_token = get_token()
    
    headers = {
        "Content-Type": "application/json",
      'Authorization': f'Bearer {bearer_token}',
      "X-Client-Version": "3.4"
    }
    
    
    response = session.post(url, json=payload, headers=headers,  params=query)
    
    data = response.json()
    print(data)
    

# create_user()

# url = "https://192.168.210.44:1280/api/v3/infrastructure/sites"

url = "https://192.168.210.44:1280/api/v3/organizations/provider"

bearer_token = get_token()

query = {
    "expand": "Organization"
}

headers = {
    "Content-Type": "application/json",
    'Authorization': f'Bearer {bearer_token}',
    "X-Client-Version": "3.4"
}

response = session.get(url, headers=headers)

data = response.json()
print(data)

