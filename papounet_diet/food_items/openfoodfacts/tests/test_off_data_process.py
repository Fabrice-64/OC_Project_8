import requests
import unittest
from django.test import TestCase
from food_items.models import Product, Store, Category
from food_items.openfoodfacts.off_data_process import ProcessStore, ProcessCategory
from food_items.openfoodfacts.config import OpenFoodFactsParams
from food_items.openfoodfacts.tests.mock_data import MockDataOFF
from unittest.mock import Mock, patch


class TestConnectionOFF(TestCase, OpenFoodFactsParams):
    def test_connexion_OFF(self):
        r = requests.get(self.URL, headers=self.HEADERS)
        self.assertEqual(r.status_code, 200)


class TestProcessStore(TestCase, ProcessStore, OpenFoodFactsParams, MockDataOFF):

    def test_download_stores(self):
        self.stores = self._download_stores()
        number_stores = self.stores.get('count')
        self.assertIsNotNone(self.stores)
        self.assertGreater(number_stores, 2000)

    @patch('requests.get')
    def test_store_full_process(self, mock_get):
        self.stores = self.from_data_to_list(self.store_data, "tags", "name")
        self._upload_stores(self.stores)
        number_stores = Store.objects.count()
        self.assertGreater(number_stores, 200)

    
class TestProcessCategory(TestCase, ProcessCategory, OpenFoodFactsParams, MockDataOFF):

    def test_download_categories(self):
        self.categories = self._download_categories()
        number_categories = self.categories.get('count')
        self.assertIsNotNone(self.categories)
        self.assertGreater(number_categories, 2000)

    @patch('requests.get')
    def test_category_full_process(self, mock_get):
        self.categories = self.from_data_to_list(self.category_data, "tags", "name")
        self._upload_categories(self.categories)
        number_categories = Category.objects.count()
        self.assertGreater(number_categories, 20)

