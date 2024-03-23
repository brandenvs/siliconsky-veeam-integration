from django.urls import path

from . import views

app_name = "backup_portal"

urlpatterns = [
    # Views
    path("", views.create_user, name="create")
    # path("", views.index, name="home"),
    # path("login/", views.user_login, name="user_login"),
    # path("register/", views.user_create, name="user_create"),
    # path("profile/", views.user_profile, name="user_profile"),
    # # Actions
    # path("auth/", views.authenticate_user, name="user_authenticate"),
    # path("registering/", views.create_user, name="create_user"),
    # path("logout/", views.logout_user, name="user_logout"),
]
