from .models import Product, BestProductSelection


def query_search_results(searched_item):
    results = Product.objects.filter(name__icontains=searched_item).order_by("nutrition_score")[:6]
    return results