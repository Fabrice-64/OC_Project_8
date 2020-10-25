from django.test import TestCase
from django.urls import resolve

from food_items.views import index

class FoodItemsURLsTestCase(TestCase):
    def test_root_url_uses_index_view(self):
        """
        Test that the root of the site resolves to the view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)