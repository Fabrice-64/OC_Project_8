from django.test import TestCase
from unittest.mock import patch
import requests


class TestOpenFoodFacts(TestCase):
    def test_connection_ok(self):
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?search_simple=1')
        self.assertEqual(r.status_code, 200)

    @patch('requests.get',)
    def test_download_stores(self):
        r = requests.get('https://fr.openfoodfacts.org/stores.json')
        stores = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertFalse(stores.get("count") < 3000)

    def test_download_categories(self):
        r = requests.get('https://fr.openfoodfacts.org/categories.json')
        categories = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertFalse(categories.get("count") < 15000)

    def test_download_products_set(self):
        pass

    def test_clean_data(self):
        pass
