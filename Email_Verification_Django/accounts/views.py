from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/')
def home(request):
    return render(request,'home.html')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        username_obj = User.objects.filter(username = username).first()
        print(username_obj)
        if username_obj is None:
            messages.error(request,"User Not Found")
            return redirect('/login_attempt')
        
        user = UserProfile.objects.filter(user = username_obj).first()
        print(user.is_verified)
        if not user.is_verified:
            messages.error(request,"Your Profile is not Verified")
            return redirect('/login_attempt')
        
        authenticate_user = authenticate(username=username,password=password)
        if authenticate_user is None:
            messages.error(request,"Wrong Password")
            return redirect('/login_attempt')
        print("Hello")
        login(request,authenticate_user)
        print("Hello")
        return redirect('/')
    
    return render(request,'login.html')


def register_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            if User.objects.filter(username = username).first():
                messages.error(request,"Username already exists")
                return redirect('/register_attempt/')
            
            if User.objects.filter(email = email).first():
                messages.error(request,"Email already exists")
                return redirect('/register_attempt/')
            
            user_obj = User.objects.create(username=username,email=email)
            user_obj.set_password(password)
            user_obj.save()

            auth_token = str(uuid.uuid4())
            profile_obj = UserProfile.objects.create(user = user_obj,auth_token = auth_token)
            profile_obj.save()
            send_email_token(email,auth_token)
            return redirect('/email_token/')
        
        except Exception as e:
            print(e)

    return render(request,'register.html')

def email_token(request):
    return render(request,'email_token.html')

def success(request):
    return render(request,'success.html')

def send_email_token(email,token):
    subject = "Verify you account (Django App)"
    message = f'Hi there,please click on this link to verify your account http://127.0.0.1:8000/verify/{token}'
    recipient_list = [email]
    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    send_mail(subject,message,email_from,recipient_list)
    
def verify(request,auth_token):
    try: 
        profile_obj = UserProfile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request,"Your Profile is already Verified")
                return redirect('/login_attempt')
            
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request,"Your profile has been verified Successfully")
            return redirect('/login_attempt')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')
    
def error(request):
    return render(request,'error.html')