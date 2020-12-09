from food_items.models import Product, Store, Category

class UploadQueries():
    def query_upload_stores(self, store_list):
        store_list = [Store(name=store) for store in store_list]
        Store.objects.bulk_create(store_list)

    def query_upload_categories(self, category_list):
        category_list = [Category(name=category) for category in category_list]
        Category.objects.bulk_create(category_list)

    def query_upload_products(self):
        pass
