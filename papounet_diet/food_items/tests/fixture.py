from food_items.models import Product, Store

def set_up_db():
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