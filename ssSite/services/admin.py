from django.contrib import admin
from django.contrib.auth.models import AbstractUser, User

from .models import VSPCUser

admin.site.register(VSPCUser)
