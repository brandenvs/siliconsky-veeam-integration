import requests, certifi, urllib3

# Setup Session
session = requests.Session()  # Provides Connection Pooling Persistence
session.verify = False  # Disable Verification
session.trust_env = False  # Prevent Tracking


# Organizations

url = "https://192.168.210.44:1280/api/v3/organizations"

query = {
  "filter": "[{\"property\":\"string\",\"items\":[{}],\"operation\":\"in\",\"collation\":\"ordinal\",\"value\":{}}]",
  "sort": "[{\"property\":\"string\",\"direction\":\"ascending\",\"collation\":\"ordinal\"}]",
  "limit": "100",
  "offset": "0",
  "select": "[{\"propertyPath\":\"string\"}]"
}

headers = {
  "X-Request-id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "X-Client-Version": "string"
}

response = requests.get(url, headers=headers, params=query)

data = response.json()
print(data)


# USER CREATE

url = "https://192.168.210.44:1280/api/v3/users"

# query = {
#   "select": "[{\"propertyPath\":\"string\"}]"
# }

payload = {
  "organizationUid": "0a093973-274b-4df8-83e2-2316dee0c9a9",
  "role": "CompanySubtenant",
  "mfaPolicyStatus": "Enabled",
  "profile": {
    "firstName": "Test",
    "lastName": "User",
    "title": "Mr",
    "email": "testuser@siliconsky.com",
    "address": None,
    "phone": "012 345 6789"
  },
  "credentials": {
    "userName": "python_testuser",
    "password": "Password1"
  },
  "backupResource": {
    "siteUid": "0107365a-60f9-422a-832b-585db173d356",
    "companySiteBackupResourceUid": "886a9551-f365-4ef7-9bcc-c227bd288369",
    "description": None,
    "vcdUserId": None,
    "resourceFriendlyName": "CloudRepo",
    "storageQuota": 100,
    "isStorageQuotaUnlimited": False
  }
}

headers = {
  "Content-Type": "application/json",
  "X-Request-id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "X-Client-Version": "string"
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
  

# import requests, certifi, urllib3

# # Setup Session
# session = requests.Session()  # Provides Connection Pooling Persistence
# session.verify = False  # Disable Verification
# session.trust_env = False  # Prevent Tracking


# url = "https://192.168.210.44:1280/api/v3/authentication/keys/rsa"

# query = {
#   "select": "[{\"propertyPath\":\"string\"}]"
# }

# headers = {
#   "X-Request-id": "ba547d14-c556-42bb-b85c-eeeb16e2f5e7",
#   "X-Client-Version": "string"
# }

# response = session.request(method='get', url=url, headers=headers)

# data = response.json()
# print(data)