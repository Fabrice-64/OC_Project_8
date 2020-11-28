from django.test import Client, TestCase
from food_items.models import Product, Store
from . import fixture as f

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
        self.assertEqual(response.status_code, 200)
        
    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
