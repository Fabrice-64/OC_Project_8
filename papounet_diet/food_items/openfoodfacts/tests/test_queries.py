"""

from food_items.openfoodfacts.queries import UploadQueries
from food_items.tests import fixture as f
from django.test import TestCase
from food_items.models import Product, Store, Category
from food_items.openfoodfacts.shared_methods import DataCleaning
import os
import json



class TestUploadQueries(TestCase, DataCleaning, UploadQueries):
    def setUp(self):
        current_path = os.path.abspath(os.getcwd())
        with open(os.path.join(current_path, "food_items/openfoodfacts/tests/off_data_to_be_tested/mock_stores.json"), 'r') as f:
            self.store_data = json.load(f)
            self.key_file = "tags"
            self.key_item = "name"

    def test_query_upload_stores(self):
        self.fail('Test Usefulness to be proven')


    def test_query__upload_categories(self):
        self.fail('Test Usefulness to be proven')

    def test_query_upload_products(self):
        self.fail('Test Usefulness to be proven')

"""