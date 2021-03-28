from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def reg(request):
    if request.method=='POST':
        username=request.POST['user_name']
        email=request.POST['email']
        First=request.POST['First']
        Last=request.POST['Last']
        password=request.POST['pass']
        confpass = request.POST['confpass']

        if password==confpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=First,last_name=Last)
                user.save()
                
                return redirect('login_page')
        else:    
            messages.info(request,'Password not matching')
            return redirect('register')
        
    else:
        return render(request,'reg.html')

        
       
def login(request):
   
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)#this like checks in DB whether the user is there or not
        if user is not None:
            auth.login(request,user) # this line is responsible for logging in. 
            return render(request,'Dashboard.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login_page')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)#this line is used for logging out 
    return redirect('/')
