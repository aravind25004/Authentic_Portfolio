from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Feature
# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    return render(request,'index.html') 


def login_view(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)

        if user is not None: 
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials invalid')
            return redirect('login')
    else:
        return render(request,"login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Alredy Used")
                return redirect('signup')
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request,"Wrong Password Check it!")
            return redirect('signup')
    else:
        return render(request,'signup.html')
    
   