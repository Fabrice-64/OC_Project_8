from django.core.management.base import BaseCommand
from food_items.openfoodfacts.queries import DeleteQueries


class Command(BaseCommand, DeleteQueries):
    help = "Empty the Database"

    def handle(self, *args, **options):
        self.query_delete_all_categories()
        self.query_delete_all_stores()
        self.query_delete_all_products()
