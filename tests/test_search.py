from pages.search_page import AirBnBSearchPage


def test_basic_search(driver):
    adults = 2
    child = 1
    location = "Rome, Italy"
    total_guests = adults + child
    search = AirBnBSearchPage(driver).load().search(location,adults,child)
    property_guest_slots = search.get_guest_slots_result()

    for guest_count in property_guest_slots:
        assert guest_count >= total_guests