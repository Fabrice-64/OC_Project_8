import requests
import unittest
from django.test import TestCase
from food_items.models import Product, Store, Category
from food_items.openfoodfacts.off_data_process import ProcessStore, ProcessCategory, ProcessProduct
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

    @patch('requests.get', autospec=True)
    def test_category_full_process(self, mock_get):
        self.categories = self.from_data_to_list(self.category_data, "tags", "name")
        self._upload_categories(self.categories)
        number_categories = Category.objects.count()
        self.assertGreater(number_categories, 20)


class TestProcessProduct(TestCase, ProcessProduct, OpenFoodFactsParams, MockDataOFF):

    def test_configure_request_payload(self):
        test_category, test_page_number = "Snacks", 1
        self.request_payload = self._configure_request_payload(test_category, test_page_number)
        self.assertEqual(self.test_payload, self.request_payload)

    def _download_products(self):
        self.mock_response= Mock(return_value=self.product_data)
        return self.mock_response.return_value
    
    def test_sort_out_product_data(self):
        data_to_sort_out = self._download_products()
        data_sorted_out = self._sort_out_product_data(data_to_sort_out)
        return data_sorted_out

    def test_clean_product_data(self):
        pass

    
        
