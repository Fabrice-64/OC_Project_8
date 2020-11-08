from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, "customer/home.html")

def register(request):
    return render(request, "customer/register.html")

def login(request):
    return render(request, "customer/login.html")

def logout(request):
    return render(request, "customer/logout.html")


