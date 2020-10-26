from django.test import Client, TestCase


class SimpleTest(TestCase):
    def test_product_details(self):
        client = Client()
        response = client.get('/food_items/product_details/')
        self.assertEqual(response.status_code, 200)

    def test_search_results(self):
        client = Client()
        response = client.get('/food_items/search_results/')
        self.assertEqual(response.status_code, 200)
