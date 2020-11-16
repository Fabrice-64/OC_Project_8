from django.test import Client, TestCase
from food_items.models import Product, Store

class SimpleTest(TestCase):
    def setUp(self):
        Store.objects.bulk_create([
            Store(name="Carrefour"),
            Store(name="Leclerc")])
        Product.objects.bulk_create([
            Product(name="Nutella Allégé",
                    brand="Nutella Ferrero",
                    code="01234567891011",
                    last_modified="2020-11-11 15:45+0200",
                    ingredients="Noisettes",
                    energy_kcal="100",
                    nutrition_score="E",
                    sugars_100g="100",
                    fat_100g="100"),
            Product(name="Nutella Délicieux",
                    brand="Nutella Ferrero",
                    code="32134567891011",
                    last_modified="2020-11-11 19:45+0200",
                    ingredients="Noisettes, Huile",
                    energy_kcal="200",
                    nutrition_score="C",
                    sugars_100g="200",
                    fat_100g="200")])
        p1 = Product.objects.get(code="01234567891011")
        p2 = Product.objects.get(code="32134567891011")
        s1 = Store.objects.get(name="Carrefour")
        s2 = Store.objects.get(name="Leclerc")
        p1.stores.set([s1, s2])
        p2.stores.set([s2])
        p1.save()
        p2.save()


    
    def test_product_details(self):
        client = Client()
        response = client.get('/food_items/product_details/01234567891011/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('food_items/product_details.html')
        product = Product.objects.get(name="Nutella Allégé")
        self.assertEqual(product.nutrition_score, "E")

    def test_searched_results(self):
        client = Client()
        response = client.post('/food_items/searched_item/', {'searched_item': 'test'})
        self.assertTemplateUsed('food_items/search_results.html')
        self.assertEqual(response.status_code, 200)
        nutella = Product.objects.get(name="Nutella Allégé")
        self.assertEqual(nutella.nutrition_score, "E")
        
    def test_record_product(self):
        client = Client()
        response = client.post('/food_items/record_product/', {'product_to_record': "01234567891011"})
        self.assertTemplateUsed('/food_items/record_product.html')
        self.assertEqual(response.status_code, 200)
        
    def test_favorites(self):
        client = Client()
        response = client.get('/food_items/favorites/')
        self.assertTemplateUsed('food_items/favorites.html')
        self.assertEqual(response.status_code, 200)
