from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
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
    return render(request, "signup.html")

def urlshortner(request):
    return HttpResponse("under work")