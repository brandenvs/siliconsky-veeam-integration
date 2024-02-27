import requests, certifi, urllib3

# Setup Session
session = requests.Session()  # Provides Connection Pooling Persistence
session.verify = False  # Disable Verification
session.trust_env = False  # Prevent Tracking


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

  if response.status_code != "200":
    print('Try Again...')       
    # Try again
    response = session.post(url=url, data=payload, headers=headers)

  print(response.headers)
  print(response.status_code, end='\n') 
  print(response.json(), end='\n')

except Exception as ex:
  print(ex)





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