from django.shortcuts import render

# Create your views here.
def make(request):
    return render(request,"home.html")