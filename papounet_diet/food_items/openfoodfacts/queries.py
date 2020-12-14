from food_items.models import Product, Store, Category
from datetime import datetime, timezone

class UploadQueries():
    def query_upload_stores(self, store_list):
        store_list = [Store(name=store) for store in store_list]
        Store.objects.bulk_create(store_list)

    def query_upload_categories(self, category_list):
        category_list = [Category(name=category) for category in category_list]
        Category.objects.bulk_create(category_list)

    def _add_products_to_db(self, product_list):
        products_to_upload = [(Product(code=item[0], brand=item[1], name=item[2],
            last_modified=datetime.fromtimestamp(int(item[3]), timezone.utc),
            nutrition_score=item[4], image_url=item[7])) for item in product_list]
        Product.objects.bulk_create(products_to_upload)
    
    def _add_stores_categories_to_product(self, product_list):
        for item in product_list:
            product = Product.objects.get(code=item[0])
            store_list = [(Store.objects.get(name=store)) for store in item[5]]
            category_list = [(Category.objects.get(name=category)) for category in item[6]]
            product.stores.set(store_list)
            product.categories.set(category_list)
            product.save()

    def query_upload_products(self, product_list):
        self._add_products_to_db(product_list)
        self._add_stores_categories_to_product(product_list)
        
        
           


                
