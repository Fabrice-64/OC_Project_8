import requests
import config as c
import json
from shared_methods import DataCleaning


class ProcessStore:
    pass


class ProcessCategory:
    pass


class ProcessProduct:
    pass


class DownloadOFF:

    def download_stores(self):
        r = requests.get(c.URL_STATIC_STORES)
        self.store_data = r.json()
        return self.store_data

    def download_categories(self):
        r = requests.get(c.URL_STATIC_CAT)
        self.category_data = r.json()
        return self.category_data

    def download_products(self):
        pass


class ProcessOFF(DataCleaning, DownloadOFF):
    def upload_stores(self):
        self.download_stores()
        self.store_list = self.from_data_to_list(self.store_data,
                                                 "tags", "name")
        self.query_upload_stores(self.store_list)


    def upload_categories(self):
        pass

    def upload_products(self):
        pass

def main():
    stores = DownloadOFF()
    res = stores.download_stores()
    print(res)

if __name__ == "__main__":
    main()