from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def registration(request):
    return HttpResponse("View Customer Registration")


def home(request):
    return render(request, 'customer/home.html')


def login(request):
    return render(request, 'customer/login.html')
