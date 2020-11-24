from django.urls import path, re_path
#from .views import ProductList
from . import views
from django.views.decorators.cache import cache_page

app_name = "food_items"

urlpatterns = [
    path("product_details/<str:product_code>/",
         views.product_details, name="product_details"),
    re_path(r'^search_results/$',
         views.search_results, 
         name="search_results"),
    path('favorites/', views.favorites, name="favorites"),
    path('record_product/', views.record_product, name="record_product"),

]
