from django.test import TestCase
import requests
import unittest


class TestOpenFoodFacts(TestCase):
    def test_connection_ok(self):
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?search_simple=1')
        self.assertEqual(r.status_code, 200)

    def test_download_static(self):
        pass

    def test_download_items(self):
        pass