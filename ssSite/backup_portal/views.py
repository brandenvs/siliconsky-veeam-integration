from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render


@login_required(login_url="web_application:login")
def index_1(request):
    return render(request, "storage_allocation_1.html")


@login_required(login_url="web_application:login")
def index_2(request):
    if request.method == "POST":

        return render(request, "storage_allocation_2.html")
