from django.shortcuts import render,redirect
from .shortener import shortner
from .models import short_urls
from .forms import UrlForm
from authenticate.models import User
# Create your views here.
def home(request, token):
    long_url= short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
def make(request):
    form=UrlForm(request.POST)
    a=''
    url=User.urls.all()
    if request.method=="POST":
        if form.is_valid():
            Newurl=form.save(commit=False)
            a= shortner().issue_token()
            Newurl.short_url=a
            Newurl.save()
        else:
            form=UrlForm()
            a="Invalid form"
    return render(request,"home.html",{
        'form':form,
        'urls':url
    })

