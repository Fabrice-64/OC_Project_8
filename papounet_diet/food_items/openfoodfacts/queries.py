from food_items.models import Product, Store, Category

class UploadQueries():
    def query_upload_stores(self, store_list):
        store_list = [Store(name=store) for store in store_list]
        Store.objects.bulk_create(store_list)

    def query__upload_categories(self):
        pass

    def query_upload_products(self):
        pass

class DisplayFromOFF():
    def display_stores(self):
        pass

    def display_categories(self):
        pass

    def display_products(self):
        pass