from django.test import Client, TestCase
from food_items.models import Product

class SimpleTest(TestCase):
    def setUp(self):
        Product.objects.create(name="Nutella Allégé",
                               brand="Nutella Ferrero",
                               code="01234567891011",
                               last_modified="2020-11-11 15:45+0200",
                               ingredients="Noisettes",
                               energy_kcal="100",
                               nutrition_score="E",
                               sugars_100g="100",
                               fat_100g="100"
                               )
        Product.objects.create(name="Nutella Délicieux",
                               brand="Nutella Ferrero",
                               code="32134567891011",
                               last_modified="2020-11-11 19:45+0200",
                               ingredients="Noisettes, Huile",
                               energy_kcal="200",
                               nutrition_score="C",
                               sugars_100g="200",
                               fat_100g="200"
                               )
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
        nutella = Product.objects.get(name="Nutella Allégé")
        self.assertEqual(nutella.nutrition_score, "E")

    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
