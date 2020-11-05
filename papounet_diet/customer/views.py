from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request, 'customer/home.html')

def registration(request):
    return HttpResponse("Page Registration")

def login(request):
    return HttpResponse('Page Login')
