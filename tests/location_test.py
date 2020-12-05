from pages.result_filter_page import AirBnBSearchPage


def test_location(driver):
    page = AirBnBSearchPage(driver).load().search()
    assert page.is_first_property_on_map()
