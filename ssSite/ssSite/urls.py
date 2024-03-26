from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web_application.urls")),
    path("backup-portal/", include("backup_portal.urls")),
]
