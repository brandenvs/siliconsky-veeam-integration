from django.urls import path

from . import views

app_name = "backup_portal"

urlpatterns = [
    # Views
    path("storage1/", views.index_1, name="demo1"),
    path("storage2/", views.index_2, name="demo2"),
]
