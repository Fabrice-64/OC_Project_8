from food_items.openfoodfacts import queries as q
from food_items.tests import fixture as f
from django.test import TestCase
from food_items.models import Product, Store, Category



class TestUploadQueries(TestCase):
    def setUp(self):
        f.set_up_db()

    def test_query_upload_stores(self):
        pass

    def test_query__upload_categories(self):
        pass

    def test_query_upload_products(self):
        pass

class TestDisplayFromOFF(TestCase):
    def setUp(self):
        f.set_up_db()

    def test_display_stores(self):
        pass

    def test_display_categories(self):
        pass

    def test_display_products(self):
        pass