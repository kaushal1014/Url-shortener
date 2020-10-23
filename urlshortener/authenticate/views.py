from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('urlshortner'))
        else:
            return HttpResponseRedirect(reverse('signup'))
    return render(request, "login.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        # password=request.POST['password'] not needed at the moment
        confirm_password=request.POST['password1']
        # email= request.POST['email']  not needed at the moment
        confirm_email= request.POST['email1']
        user=User.objects.create_user(username=username, password=confirm_password, email=confirm_email)
        user.save()
        return HttpResponseRedirect(reverse('urlshortner'))

    return render(request, "signup.html")

def urlshortner(request):
    return HttpResponse("under work")