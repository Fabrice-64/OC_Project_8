from django.test import Client, TestCase
from food_items.models import Product, Store
from django.contrib.auth.models import User
from . import fixture as f
from django.shortcuts import reverse
from food_items import queries as q


class SimpleTest(TestCase):
    def setUp(self):
        f.set_up_db()

    def test_product_details(self):
        client = Client()
        response = client.get('/food_items/product_details/01234567891011/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('food_items/product_details.html')

    def test_search_results(self):
        client = Client()
        response = client.get('/food_items/search_results/', {'searched_item': 'test'})
        self.assertTemplateUsed('food_items/search_results.html')
        self.assertEqual(response.status_code, 200)
        
    def test_record_product(self):
        client = Client()
        response = client.get('/food_items/record_product/01234567891011/')
        product_to_record = Product.objects.get(code='01234567891011')
        user = request.user
        q.query_record_best_product(product_to_record, user)
        self.assertEqual(response.status_code, 200)
    
        
    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
