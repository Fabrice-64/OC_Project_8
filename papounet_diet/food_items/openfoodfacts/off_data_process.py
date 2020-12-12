import requests
import json
from food_items.openfoodfacts.shared_methods import DataCleaning
from food_items.openfoodfacts.config import OpenFoodFactsParams
from food_items.openfoodfacts.queries import UploadQueries


class ProcessStore(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _download_stores(self):
        response = requests.get(self.URL_STORES)
        return response.json()

    def _upload_stores(self, stores):
        self.query_upload_stores(stores)

    def store_full_process(self):
        self.stores = self._download_stores()
        self.stores = self.from_data_to_list(self.stores, "tags", "name")
        self._upload_stores(self.stores)


class ProcessCategory(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _download_categories(self):
        response = requests.get(self.URL_CATEGORIES)
        return response.json()

    def _upload_categories(self, categories):
        self.query_upload_categories(categories)
    
    def category_full_process(self):
        self.categories = self._download_categories()
        self.categories = self.from_data_to_list(self.categories, "tags", "name")
        self._upload_categories(self.categories)
        


class ProcessProduct(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _configure_request_payload(self, category, page_number):
        self.payload.update({"tag_0": category})
        self.payload.update({"page": page_number})
        return self.payload
    
    def _download_products(self):
        r = requests.get(self.URL, headers=self.HEADERS, params=self.payload)
        self.product_data = r.json()
        return self.product_data

    def _sort_out_product_data(self, product_data):
        products_list = list()
        for product in product_data["products"]:
            brand = product.get('brands')
            name = product.get('product_name')
            code = product.get('code')
            nutrition_grade_fr = product.get('nutrition_grade_fr')
            stores = product.get('stores').split(",")
            categories = product.get('categories').split(",")
            image_url = product.get('image_url')
            products_list.append((code, brand, name, nutrition_grade_fr, stores, categories, image_url))
        return products_list

    def product_full_process(self, category, page_number):
        self._configure_request_payload(category, page_number)
        product_data = self._download_products()
        self.sort_out_product_data(product_data)



    

