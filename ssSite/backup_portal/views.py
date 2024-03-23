from django.shortcuts import render


def create_user(request):
    return render(request, "create_user.html")
