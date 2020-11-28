from food_items import queries as q
from . import fixture as f
from django.test import Client, TestCase
from food_items.models import Product, BestProductSelection
from django.contrib.auth.models import User
from . import fixture as f

class QueriesTest(TestCase):
    def setUp(self):
        f.set_up_db()

    def test_query_search_results(self):
        result = q.query_search_results('Nutella')
        self.assertIsNotNone(result)

    def test_query_record_best_product(self):
        length = len(BestProductSelection.objects.all())
        product_to_record = Product.objects.get(code='01234567891011')
        user = User.objects.get(username='user')
        q.query_record_best_product(product_to_record, user)
        n_length = len(BestProductSelection.objects.all())
        self.assertEqual(length+1, n_length)