from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def product_details(request):
    return HttpResponse("Hello, page product_details de food_items")


def search_results(request):
    return HttpResponse("Hello, page search_results de food_items")
