from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from .models import Product

# Create your views here.


def product_details(request, product_name):
    context = {'product_name': product_name}
    return render(request, "food_items/product_details.html", context)


def search_results(request):
    searched_item = request.POST['searched_item']
    results = Product.objects.filter(name__contains=searched_item)
    context = {'search_results': results, 'searched_item': searched_item}
    return render(request, "food_items/search_results.html", context)

def favorites(request):
    return render(request, "food_items/favorites.html")
