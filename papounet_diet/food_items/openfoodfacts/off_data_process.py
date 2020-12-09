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
        


class ProcessProduct:
    pass
