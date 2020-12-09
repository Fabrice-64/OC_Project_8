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

    
