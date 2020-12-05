from pages.result_filter_page import AirBnBFilterPage


def test_filter_search(driver):
    no_bedrooms = 5
    search = AirBnBFilterPage(driver).load().filter(no_bedrooms)
    properties_bedroom_slots = search.get_bedroom_count_result()
    for bedroom_count in properties_bedroom_slots:
        assert bedroom_count >= no_bedrooms

    assert search.is_there_pool_in_first_property()
