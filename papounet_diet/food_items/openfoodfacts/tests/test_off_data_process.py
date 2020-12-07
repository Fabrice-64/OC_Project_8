import requests
from django.test import TestCase
from food_items.models import Product, Store, Category
from food_items.openfoodfacts.off_data_process import ProcessStore
from food_items.openfoodfacts.config import OpenFoodFactsParams


class TestProcessStore(TestCase, ProcessStore, OpenFoodFactsParams):

    def test_connexion_OFF(self):
        r = requests.get(self.URL, headers=self.HEADERS)
        self.assertEqual(r.status_code, 200)

    
    def test_download_stores(self):
        self.stores = self._download_stores()
        number_stores = self.stores.get('count')
        self.assertIsNotNone(self.stores)
        self.assertGreater(number_stores, 2000)

    



"""
def test_download_products(self):
        self.fail('Test non completed')
def test_download_categories(self):
        self.categories = self.download_categories()
        number_categories = self.categories.get('count')
        self.assertIsNotNone(self.categories)
        self.assertGreater(number_categories, 2000)

class TestUploadData(TestCase, ManageOFF, UploadQueries):

    def setUp(self):
        current_path = os.path.abspath(os.getcwd())
        with open(os.path.join(current_path, "food_items/openfoodfacts/tests/off_data_to_be_tested/mock_stores.json"), 'r') as f:
            self.store_data = json.load(f)
            self.key_file = "tags"
            self.key_item = "name"

    # double with test_query
    def test_upload_stores(self):
        number_stores = Product.objects.count()
        self.store_list = self.from_data_to_list(self.store_data,
                                                 self.key_file, self.key_item)
        self.query_upload_stores(self.store_list)
        new_number = Store.objects.count()
        self.assertGreater(new_number, 100)


    def test_upload_categories(self):
        self.fail('Test non completed')

    def test_upload_products(self):
        self.fail('Test non completed')
"""