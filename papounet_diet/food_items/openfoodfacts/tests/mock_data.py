import os
import json



current_path = os.path.abspath(os.getcwd())
def get_mock_data(mock_data):
    with open(os.path.join(current_path, "food_items/openfoodfacts/tests/off_data_to_be_tested/", mock_data), 'r') as f:
        mock_data = json.load(f)
    return mock_data


class MockDataOFF:
    
    store_data = get_mock_data("mock_stores.json")

    category_data = get_mock_data("mock_categories.json")

    product_data = get_mock_data("mock_products.json")

    test_payload = {
          'tagtype_0': 'categories', 'tag_contains_0': 'contains',
          'tag_0': 'Snacks', 'tag_types_1': 'countries',
          'tag_contains_1': 'contains', 'tag_1': 'fr',
          'json': 1, 'action': "process",
          "page_size": 1000, 'page': 1
           }

    
