from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        FirstName = request.POST.get('firstname')
        LastName = request.POST.get('lastname')
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = User.objects.filter(email = Email).first()
        if user:
            context = {'error': 'User already exists'}
            return render(request,'auth/register.html',context)
        
        user = User(first_name = FirstName, last_name = LastName, email = Email, username = Email)
        user.set_password(Password)
        user.save()

        
    return render(request,'auth/register.html')

def auth_login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')

        user = User.objects.filter( email = Email).first()
        if not user:
            context = {'error': 'User Does not exists'}
            return render(request,'auth/login.html',context)
        
        user = authenticate(username = Email,password = Password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:   
            context = {'error': 'Invalid Credentials'}
            return render(request,'auth/login.html',context)

    return render(request,'auth/login.html')

def logout_page(request):
    logout(request)
    return redirect('/auth/login')

