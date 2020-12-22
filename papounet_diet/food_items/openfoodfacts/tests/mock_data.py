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

    
class MockProducts:
    mock_product_list = [
        ('Bjorg',
        "P'tit Nature Complet",
        '3229820021027',
        'b',
        ['Magasins U'],
        ['Snacks', 'Snacks sucrés', 'Biscuits et gâteaux', 'Biscuits', 'Petit-déjeuners'],
        'https://static.openfoodfacts.org/images/products/322/982/002/1027/front_fr.135.400.jpg',
        1602617804,
        ),
        ('LU',
        'TUC Original',
         '5410041001204',
         'd',
         ['Carrefour', 'Magasins U', 'REWE'],
         ['Snacks', 'Snacks salés', 'Snacks sucrés', 'Biscuits et gâteaux', 'Biscuits'], 
         'https://static.openfoodfacts.org/images/products/541/004/100/1204/front_fr.97.400.jpg',
         1607767361,
         )
        ]