from food_items.openfoodfacts.data_cleaning import DataCleaning
from django.test import TestCase
import os, sys
import pathlib
import json


class TestDataCleaning(TestCase, DataCleaning):
    def test_check_special_characters(self):
        values = ["",
                  "le-magasin",
                  "l'autre magasin"]
        test_list = []
        for value in values:
            result = self._check_special_characters(value)
            test_list.append(result)
        self.assertIsNotNone(result)
        self.assertEqual(test_list, ["NaN", "le magasin", "l\'autre magasin"])


    def test_from_data_to_list(self):
        current_path = os.path.abspath(os.getcwd())
        with open(os.path.join(current_path, "food_items/openfoodfacts/tests/off_data_to_be_tested/mock_stores.json"), 'r') as f:
            data = json.load(f)
        key_file = "tags"
        key_item = "name"
        store_list = self.from_data_to_list(data, key_file, key_item)
        self.assertGreater(len(store_list), 10)
        return store_list