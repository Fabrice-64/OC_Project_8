
import os

class OpenFoodFactsParams:

    URL = 'https://fr.openfoodfacts.org/cgi/search.pl?'

    HEADERS = {'User-Agent': 'python-requests/2.22.0'}

    URL_STATIC = 'https://fr.openfoodfacts.org/'

    URL_STORES = os.path.join(URL_STATIC, 'stores.json')

    URL_CATEGORIES = os.path.join(URL_STATIC, 'categories.json')

