from django.urls import path, re_path

from . import views

app_name = "food_items"

urlpatterns = [
    path("product_details/<str:product_code>/",
         views.product_details, name="product_details"),
    path('searched_item/',
         views.search_results, name="searched_item"),
    path('favorites/', views.favorites, name="favorites"),

]
