import requests
import json
from food_items.openfoodfacts.shared_methods import DataCleaning
from food_items.openfoodfacts.config import OpenFoodFactsParams


class ProcessStore(DataCleaning, OpenFoodFactsParams):
    def _download_stores(self):
        response = requests.get(self.URL_STORES)
        return response.json()

    def _upload_stores(self, stores):
        self.query_upload_stores(stores)

    def store_full_process(self):
        stores = self._download_stores()
        stores = self.from_data_to_list(stores, "tags", "name")
        self._upload_stores(stores)


class ProcessCategory:
    def _download_categories(self):
        r = requests.get(self.URL_CATEGORIES)
        self.category_data = r.json()
        return self.category_data

    def _upload_category(self):
        pass


class ProcessProduct:
    pass
