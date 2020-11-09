from django.test import Client, TestCase


class SimpleTest(TestCase):
    def test_product_details(self):
        client = Client()
        response = client.get('/food_items/product_details/test/')
        self.assertTemplateUsed('food_items/product_details.html')
        self.assertEqual(response.status_code, 200)

    def test_searched_item(self):
        client = Client()
        response = client.post('/food_items/searched_item/', {'searched_item': 'test'})
        self.assertTemplateUsed('food_items/search_results.html')
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
