from django.shortcuts import render, redirect

from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def user_login(request):
    if request.user.is_authenticated:
        return redirect('web_application:home')
    else:
        return render(request, 'login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']

    # Lowercase username
    username_lower = str(username).lower()

    # Authorize user
    user = authenticate(username=username_lower, password=password)
    # User is NOT Authenticated
    if user is None:
        # Update result parameter to pass to view
        error_message = "Invalid Username or Password!"
        # Construct reverse URL for Http Response Redirect
        return render(request, 'login.html', {'error_message': error_message})
    else:
        # Login user 
        login(request, user)
        return HttpResponseRedirect(reverse('web_application:home'))

@login_required(login_url='web_application:user_login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='web_application:user_login')
def user_profile(request):
    return render(request, 'user.html')

@login_required(login_url='web_application:user_login')
def user_create(request):
    return render(request, 'create_user.html')

@login_required(login_url='web_application:user_login')
def create_user(request):
    if request.method == 'POST':
        # Fetch User Details from Web Page
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        full_name = str(fullname).split(' ')

        first_name	= full_name.pop(0)
        last_name = ' '.join(full_name)

        try:
            # Create a New User instance and Set Attributes
            new_user = User.objects.create_user(username=username, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.is_staff = False
            new_user.is_superuser = False

            # Save User to Database
            new_user.save()
            # Redirect User to Profile
            return redirect('web_application:home')   
        
        # Catch the exception
        except Exception as ex:
            # Render Create User View and, Pass the Error Message to View
            return render(request, 'create_user.html', {'error_message': str(ex)})
    
    # Render Initial Create User View
    return render(request, 'create_user.html')

@login_required(login_url='web_application:user_login')
def logout_user(request):
    logout(request)
    return redirect('web_application:user_login')