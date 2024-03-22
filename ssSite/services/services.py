import time

from django.conf import settings
from requests import Session

from .models import TenantUser


class SessionManager:
    def __init__(self, request):
        self.request = request
        self.session = Session()

    def get_session(self):
        api_user = TenantUser.objects.get(user=self.request.user)

        self.session.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_user.access_token}",
            "Accept-Encoding": "gzip",
        }
        return self.session

    def get_token(self):
        url = "https://192.168.210.44:1280/api/v3/token"

        payload = {
            "grant_type": "password",
            "username": r"demo_zero_one\api_user",
            "password": "S1l1conSky@DEV",
        }

        headers = {"X-Client-Version": "3.4"}

        try:
            response = self.session.post(url=url, data=payload, headers=headers)

            json_response = response.json()

            print(json_response)

            bearer_token = json_response["access_token"]

            return bearer_token

        except Exception as ex:
            return print(ex)


class TenantUserManager:
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def create_apiuser(self):
        api_user = TenantUser(user=self.request.user)

        api_user.save()
        print("[SUCCESS] Created API User!")

    def auth_credentials():
        # Define Auth URL
        auth_url = "https://customerapiauth.fortinet.com/api/v1/oauth/token/"

        # Define Request Headers
        headers = {
            "Content-Type": "application/json",
        }

        # Define JSON Payload
        payload = {
            "username": settings.API_KEY,
            "password": settings.PASSWORD,
            "client_id": settings.CLIENT_ID,
            "grant_type": "password",
        }

        try:
            response = session.post(
                auth_url, headers=headers, json=payload, verify=False
            )
            if response.status_code == 200:
                print(
                    "[SUCCESS] FortiAuthenticator Authorized Bearer & Refresher Tokens -- ",
                    response.status_code,
                    end="\n",
                )
                # If authentication is successful, create APIUser
                api_user_creator = APIUserCreator(request, response)
                api_user_creator.create_apiuser()
            else:
                print(
                    "[ERROR] FortiAuthenticator was Unable to Authorize Bearer & Refresher Tokens -- ",
                    {response.status_code},
                    end="\n",
                )
            return response

        except Exception as e:
            print(
                f"[ERROR] FortiAuthenticator Unable to Authenticate User Credentials...\nUnexpected Error: {e}\n"
            )
            return 404
