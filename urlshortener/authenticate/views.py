from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#from django.contrib.auth.models import User
from .models import User
from urlhandel.views import make
# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists() and User.objects.filter(password=password).exists():
             return HttpResponseRedirect(reverse('authenticate:urlshortner'))
        else:
            return HttpResponseRedirect(reverse('authenticate:signup'))
    return render(request, "login.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        # password=request.POST['password'] not needed at the moment
        confirm_password=request.POST['password1']
        # email= request.POST['email']  not needed at the moment
        confirm_email= request.POST['email1']
        
        user=User(username=username,password=confirm_password,email=confirm_email)
        user.save()
        return HttpResponseRedirect(reverse('authenticate:urlshortner'))

    return render(request, "signup.html")

def urlshortner(request):
    return make(request)