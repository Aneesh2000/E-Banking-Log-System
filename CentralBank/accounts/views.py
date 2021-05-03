from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponse
from profiles.models import Status 
from django.contrib.auth.models import User

import logging 

logger = logging.getLogger('django')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('user registered sucessfully')
            return redirect("accounts:signin")
    else:
        form = UserCreationForm()
    return render(request, "accounts/create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":    

          

         
        form = AuthenticationForm(data=request.POST)
       

        
        if form.is_valid():
            user = form.get_user()
            #return render(request,"index.html")
            login(request, user)
            ip = get_client_ip(request)
            username = request.user.get_username()
            user = User.objects.get(username=username)
            
            try:
                curr_user = Status.objects.get(user_name=username)

                z = 'user: '+username+" account_no: "+str(curr_user.account_number)+ ' Logged_In Successfully '+'ip_address: '+str(ip)
                logger.info(z)
            except Status.DoesNotExist:
                logger.info("new user :"+str(username)+' logged in.')
            return redirect("profiles:account_status")
        else:
            logger.error('Error while user getting loggedin')
            return render(request,"index.html")

    else:
        form = AuthenticationForm()
        #return redirect("accounts:sign_in.html")
        return render(request, "accounts/sign_in.html", {"form": form})
    
        
        

def logout_view(request):
    # Logout the user if he hits the logout submit button
    logout(request)
    logger.info('user Logged-out sucessfully')
    return redirect("accounts:signin")
