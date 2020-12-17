from django.core.management.base import BaseCommand
from food_items.openfoodfacts.off_data_process import ProcessStore, ProcessCategory, ProcessProduct


class Command(BaseCommand, ProcessCategory, ProcessStore, ProcessProduct):
    help = "DB initialization for first use"

    def handle(self,*args, **options):
        stores = ProcessStore()
        stores.store_full_process()

        categories = ProcessCategory()
        categories.category_full_process()

        products = ProcessProduct()
        products.manage_full_set_products()