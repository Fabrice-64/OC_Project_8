from food_items.openfoodfacts import queries as q
from food_items.tests import fixture as f
from django.test import TestCase
from food_items.models import Product, Store, Category



class TestDownloadFromOFF(TestCase):

    def test_connexion_OFF(self):
        pass

    def test_download_stores(self):
        pass

    def test_download_categories(self):
        pass

    def test_download_products(self):
        pass


class TestUploadToDB(TestCase):
    def setUp(self):
        f.set_up_db()

    def test_upload_stores(self):
        pass

    def test_upload_categories(self):
        pass

    def test_upload_products(self):
        pass
