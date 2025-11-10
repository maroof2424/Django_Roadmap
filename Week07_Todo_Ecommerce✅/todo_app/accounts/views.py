from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User Created Successfully...")    
            return redirect("list_tasks")
    else:
        form = RegisterForm()
    return render(request,"accounts/register.html",{"form":form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"User Logined Successfully...")    
            return redirect("list_tasks")
        else:
            messages.error(request,"Invalid crediantials...")
    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{"form":form})


def logout_user(request):
    logout(request)
    messages.success(request,"User Logined Successfully...")
    return redirect("login")
    
