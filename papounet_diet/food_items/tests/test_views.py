from django.test import Client, TestCase, RequestFactory
from food_items.models import Product, Store
from django.contrib.auth.models import User
from . import fixture as f
from django.shortcuts import reverse
from food_items import queries as q
from food_items import views as v


class SimpleTest(TestCase):
    def setUp(self):
        f.set_up_db()
        self.factory = RequestFactory()
        self.user = User.objects.get(username="user")

    def test_product_details(self):
        request = self.factory.get('/food_items/product_details')
        response = v.product_details(request, "01234567891011")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('food_items/product_details.html')

    def test_search_results(self):
        request = self.factory.get('/food_items/search_results/')
        request.user = self.user
        response = v.search_results(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('food_items/search_results.html')

    def test_record_product(self):
        request = self.factory.get('food_items/record_product/')
        request.user = self.user
        response = v.record_product(request, "01234567891011")
        # code 302 due to a redirection in the record_product view
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('food_items/search_results.html')

    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
