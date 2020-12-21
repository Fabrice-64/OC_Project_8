from .models import Product, BestProductSelection
from django.core.cache import cache
from django.shortcuts import render, redirect, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from food_items import queries as q


def product_details(request, product_code):
    product_details, stores = q.query_product_details(product_code)
    context = {'product_details': product_details, 'stores': stores}
    return render(request, "food_items/product_details.html", context)


def favorite_details(request, product_code):
    product_details, stores = q.query_product_details(product_code)
    context = {'product_details': product_details, 'stores': stores}
    return render(request, "food_items/favorite_details.html", context)


def search_results(request):
    try:
        searched_item = request.GET['searched_item']
        results = q.query_search_results(searched_item)
        context = {'search_results': results, 'searched_item': searched_item }
        cache.set('cache_results', context)
        return render(request, "food_items/search_results.html", context)
    except MultiValueDictKeyError:
        context = cache.get('cache_results')
        return render(request, "food_items/search_results.html", context)


def record_product(request, product_code):
    q.query_record_best_product(product_code, request.user)
    return redirect(reverse("food_items:search_results"))


def fetch_favorites(request):
    favorites = q.query_fetch_favorites(request.user)
    context = {'favorites': favorites}
    return render(request, "food_items/favorites.html", context)


