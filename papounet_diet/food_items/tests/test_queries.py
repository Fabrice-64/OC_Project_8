from food_items import queries

def test_query_search_results():
    result = queries.query_search_results('Nutella')
    assert result is not None