from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

from .models import Product

# Create your views here.

def product_details(request, product_code):
    product_details = Product.objects.get(code=product_code)
    stores = ", ".join([store.name for store in product_details.stores.all()])
    context = {'product_details': product_details, 'stores': stores}
    return render(request, "food_items/product_details.html", context)


def search_results(request):
    searched_item = request.POST['searched_item']
    results = Product.objects.filter(name__contains=searched_item).order_by("nutrition_score")[:6]
    context = {'search_results': results, 'searched_item': searched_item}
    return render(request, "food_items/search_results.html", context)

def record_product(request):
    product_to_record = request.POST['product_to_record']

    return render(request, "food_items/record_product.html")

def favorites(request):
    return render(request, "food_items/favorites.html")


