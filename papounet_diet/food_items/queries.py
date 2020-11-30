from .models import Product, BestProductSelection


def query_search_results(searched_item):
    results = Product.objects.filter(name__icontains=searched_item).order_by("nutrition_score")[:6]
    return results

def query_record_best_product(product_to_record, user):
    new_favorite = BestProductSelection(code=product_to_record, user=user)
    new_favorite.save()

def query_fetch_favorites(user):
    favorites = Product.objects.filter(selection__username="user").distinct("code")[:6]
    return favorites

def query_product_details(product_code):
    product_details = Product.objects.get(code=product_code)
    stores = ", ".join([store.name for store in product_details.stores.all()])
    return product_details, stores
