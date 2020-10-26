from django.urls import path

from . import views

urlpatterns = [
    path('product_details/',
         views.product_details, name="product_details"),
    path('search_results/',
         views.search_results, name="search_results"),
]
