from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from base.email import send_custom_email
from .models import Profile

def register_page(request):
    if request.method=="POST":
        # we are using email as username
        data=request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email=data.get('email')
        password=data.get('password')
        
        user = User.objects.filter(username=email).exists()
        
        print("Values are ",first_name," " ,last_name," " ,email," " ,password)
        
        if user:
            messages.error(request, "Username already exists")
            return HttpResponseRedirect(request.path_info)
        
        user=User.objects.create(first_name=first_name, last_name=last_name, username=email)
        
        user.set_password(password)
        user.save()
        
        messages.success(request, "An email has been sent on your mail.")
        return HttpResponseRedirect(request.path_info)
    else:
        content={"user":"Guest"}
        return render(request, "pages/accounts/register.html", content)
    

def login_page(request):
    
    if request.method=="POST":
        data=request.POST
        email=data.get('email')
        password=data.get('password')
        
        user = User.objects.filter(username=email)
        
        if not user.exists():
            messages.error(request, "Invalid email")
            return HttpResponseRedirect(request.path_info)
        
        print(user[0].profile)
        # here need to write code for email verification
        if not user[0].profile.is_email_verified:
            messages.error(request, "Register your email")
            return HttpResponseRedirect(request.path_info)
        
        user=authenticate(username=email, password=password)
        if not user:
            messages.error(request, "Invalid password")
            return HttpResponseRedirect(request.path_info)
        
        login(request,  user)
        return redirect('/')
    else:
        content={"user":"Guest"}
        return render(request, "pages/accounts/login.html", content)
     
def logout_page(request):
    logout(request)
    return redirect('/accounts/login/')
     

def user_account_verification(request, email_token):
    user = Profile.objects.filter(email_token=email_token)
    
    if not user.exists():
        return HttpResponse("Not a vlid token")
    else: 
        user = user[0]
        user.is_email_verified=True
        user.save()
        return redirect("/accounts/login/")

def home(request):
    messages.success(request, "Logout Successfully.")
    return render(request, 'index.html')
