from food_items.models import Product, Store, Category
from datetime import datetime, timezone

class UploadQueries():
    def query_upload_stores(self, store_list):
        store_list = [Store(name=store) for store in store_list]
        Store.objects.bulk_create(store_list)

    def query_upload_categories(self, category_list):
        category_list = [Category(name=category) for category in category_list]
        Category.objects.bulk_create(category_list)

    def query_upload_products(self, product_list):
        products_to_upload= list()
        for item in product_list:
            products_to_upload.append(Product(code=item[0], brand=item[1], name=item[2],
                                last_modified=datetime.fromtimestamp(int(item[3]), timezone.utc),
                                nutrition_score=item[4], image_url=item[7]))
            
        Product.objects.bulk_create(products_to_upload)
        return products_to_upload
