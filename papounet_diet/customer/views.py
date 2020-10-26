from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def registration(request):
    return HttpResponse("View Customer Registration")


def home(request):
    return HttpResponse("Hello. Page home de customer")


def login(request):
    return HttpResponse("Hello. page login de customer")