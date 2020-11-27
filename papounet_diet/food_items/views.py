from .models import Product, BestProductSelection
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate
from django.http import HttpResponse

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
    print(product_to_record.name)
    return HttpResponse('OK Record Product')

def favorites(request):
    return render(request, "food_items/favorites.html")
