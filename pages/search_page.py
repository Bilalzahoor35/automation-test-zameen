from selenium.webdriver.common.by import By
from pages.common import wait_until_located, click


class AirBnBSearchPage:
    URL = 'https://www.airbnb.com/'

    SEARCH_INPUT = (By.ID, 'bigsearch-query-detached-query')
    GUEST_BTN = (By.CSS_SELECTOR, '[data-testid="structured-search-input-field-guests-button"]')
    ADULT_COUNT_PLUS = (By.CSS_SELECTOR, '[data-testid="stepper-adults-increase-button"]')
    CHILD_COUNT_PLUS = (By.CSS_SELECTOR, '[data-testid="stepper-children-increase-button"]')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-testid="structured-search-input-search-button"]')
    RESULT_DIV =(By.CLASS_NAME, '_fhph4u')
    PROPERTY_DIV = (By.XPATH,'//*[@class="_kqh46o"]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        return self

    def search(self,location,adults_count=2,child_count=1):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(location)

        wait_until_located(self.driver,*self.GUEST_BTN)
        guest_button = self.driver.find_element(*self.GUEST_BTN)
        click(guest_button)

        wait_until_located(self.driver,*self.ADULT_COUNT_PLUS)
        adult_button = self.driver.find_element(*self.ADULT_COUNT_PLUS)
        click(adult_button, adults_count)

        wait_until_located(self.driver,*self.CHILD_COUNT_PLUS)
        child_button = self.driver.find_element(*self.CHILD_COUNT_PLUS)
        click(child_button,child_count)

        search_button = self.driver.find_element(*self.SEARCH_BTN)
        click(search_button)
        print("Here")
        return self

    def get_guest_slots_result(self):
        property_guests_slots = []
        wait_until_located(self.driver, *self.RESULT_DIV,30)
        search_results = self.driver.find_elements(*self.PROPERTY_DIV)
        for result in search_results:
            text: str = result.text
            if "guests" in text:
                property_guests_slots.append(int(text[0:2]))
        return property_guests_slots