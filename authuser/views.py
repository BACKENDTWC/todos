from django.shortcuts import render, redirect
from authuser.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

"""
User ( User Table)
- username (varchar)
- password (varchar)(hashed)
- email
- is_active
- is_staff
- is_superuser
- date_joined
- last_login

"""

# Create your views here.

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        messages.success(request,"Registered Successfully")
        return render(request,"success_register.html")
    else:
        return render(request,"register.html")
    

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            messages.success(request,"Login Successful")
            return redirect("/todos")
        else:
            messages.error(request,"invalid credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")


