import time

from django.conf import settings
from requests import Session

from .models import VSPCUser


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
