from .models import Product, BestProductSelection
from django.core.cache import cache
from django.shortcuts import render, redirect, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.models import User
from food_items import queries as q

# Create your views here.

def product_details(request, product_code):
    product_details = Product.objects.get(code=product_code)
    stores = ", ".join([store.name for store in product_details.stores.all()])
    context = {'product_details': product_details, 'stores': stores}
    return render(request, "food_items/product_details.html", context)


def search_results(request):
    if request.user.is_authenticated is True:
        authentication = "ok"
    else:
        authentication = "nok"
    try:
        searched_item = request.GET['searched_item']
        results = Product.objects.filter(name__icontains=searched_item).order_by("nutrition_score")[:6]
        context = {'search_results': results, 'authentication': authentication}
        cache.set('cache_results', context)
        return render(request, "food_items/search_results.html", context)
    except MultiValueDictKeyError:
        context = cache.get('cache_results')
        return render(request, "food_items/search_results.html", context)

def record_product(request, product_code):
    product_to_record = Product.objects.get(code=product_code)
    user = request.user
    q.query_record_best_product(product_to_record, user)
    return redirect(reverse("food_items:search_results"))

def favorites(request):
    return render(request, "food_items/favorites.html")
