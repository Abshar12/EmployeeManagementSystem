from django.shortcuts import render
from .models import *
from django.contrib.auth import logout , authenticate , login 
from django.shortcuts import render , redirect
from cryptography.fernet import Fernet
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request , 'index.html')


def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request,email=email,password=password)
        print ( user is not None)
        if user is not None:
            login(request,user)
            
            return render(request,'welcome.html')

        
    else:
        return render(request,'admin_login.html')
    
    return render(request,'admin_login.html')


def admin_logout(request):
    logout(request)

