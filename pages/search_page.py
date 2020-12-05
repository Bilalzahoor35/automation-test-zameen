from selenium.webdriver.common.by import By
from pages.common import wait_until_located, click, move_to_element


class AirBnBSearchPage:
    URL = 'https://www.airbnb.com/'

    SEARCH_INPUT = (By.ID, 'bigsearch-query-detached-query')

    GUEST_BTN = (By.CSS_SELECTOR, '[data-testid="structured-search-input-field-guests-button"]')
    ADULT_COUNT_PLUS = (By.CSS_SELECTOR, '[data-testid="stepper-adults-increase-button"]')
    CHILD_COUNT_PLUS = (By.CSS_SELECTOR, '[data-testid="stepper-children-increase-button"]')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-testid="structured-search-input-search-button"]')

    # These html elements don't have any identifying attributes therefore we're using class names as selector
    RESULT_DIV = (By.CLASS_NAME, '_fhph4u')
    PROPERTY_DIVS = (By.XPATH, '//*[@class="_kqh46o"]')
    PROPERTY_RENT = (By.CLASS_NAME, '_1p7iugi')
    MAP_TAGS = (By.CLASS_NAME, '_1nq36y92')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        return self

    def search(self, location="Rome, Italy", adults_count=2, child_count=1):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(location)

        wait_until_located(self.driver, *self.GUEST_BTN)
        guest_button = self.driver.find_element(*self.GUEST_BTN)
        click(guest_button)

        wait_until_located(self.driver, *self.ADULT_COUNT_PLUS)
        adult_button = self.driver.find_element(*self.ADULT_COUNT_PLUS)
        click(adult_button, adults_count)

        wait_until_located(self.driver, *self.CHILD_COUNT_PLUS)
        child_button = self.driver.find_element(*self.CHILD_COUNT_PLUS)
        click(child_button, child_count)

        search_button = self.driver.find_element(*self.SEARCH_BTN)
        click(search_button)
        return self

    def get_guest_slots_result(self):
        property_guests_slots = []
        wait_until_located(self.driver, *self.RESULT_DIV, 30)
        search_results = self.driver.find_elements(*self.PROPERTY_DIVS)
        for result in search_results:
            text: str = result.text
            if "guests" in text:
                property_guests_slots.append(int(text[0:2]))
        return property_guests_slots

    def is_first_property_on_map(self):
        wait_until_located(self.driver, *self.RESULT_DIV)
        properties = self.driver.find_elements(*self.PROPERTY_DIVS)
        move_to_element(self.driver, properties[0])

        # Returns first property rent element
        first_property_rent = wait_until_located(self.driver, *self.PROPERTY_RENT).text
        return self.__is_first_property_rent_on_map(first_property_rent)

    def __is_first_property_rent_on_map(self, rent):
        try:
            # returns location pin for fist property
            location_tag = wait_until_located(self.driver, *self.MAP_TAGS, timeout=10).text.replace("\n", "")
            if location_tag in rent:
                return True
        except:
            pass
        return False
