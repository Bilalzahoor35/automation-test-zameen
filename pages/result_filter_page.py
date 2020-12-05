from selenium.webdriver.common.by import By
from pages.common import wait_until_located, move_to, click, wait_until_refresh
from .search_page import AirBnBSearchPage


class AirBnBFilterPage:
    FILTER_MENU_BTN = (By.ID, 'menuItemButton-dynamicMoreFilters')
    RESULT_DIV = (By.CLASS_NAME, '_fhph4u')
    PROPERTY_DIVS = (By.XPATH, '//*[@class="_kqh46o"]')
    PROPERTY_CLICKABLE_DIVS = (By.XPATH, '//*[@class="_gjfol0"]')

    BED_ROOM_BTN_PLUS = (
        By.CSS_SELECTOR, '[data-testid="filterItem-rooms_and_beds-stepper-min_bedrooms-0-increase-button"]')
    APARTMENT_PROPERTIES_DIV = (By.XPATH, '//*[@name="Apartment"]')
    AMENITIES_DIV = (By.CLASS_NAME, '_1tv4hg3')
    AMENITIES_LIST = (By.CLASS_NAME, '_1seuw5go')
    POOL_CHECK_BOX = (By.NAME, 'Pool')
    SHOW_FILTER_RESULT_BTN = (By.CSS_SELECTOR, '[data-testid="more-filters-modal-submit-button"]')

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        # Opening Filter Page
        AirBnBSearchPage(self.driver).load().search()
        return self

    def filter(self, bed_rooms=5):
        wait_until_located(self.driver, *self.RESULT_DIV)
        filter_btn = self.driver.find_element(*self.FILTER_MENU_BTN).find_elements_by_tag_name("button")[0]
        click(filter_btn)

        bed_rooms_btn = wait_until_located(self.driver, *self.BED_ROOM_BTN_PLUS)
        click(bed_rooms_btn, bed_rooms)
        move_to(self.driver, *self.APARTMENT_PROPERTIES_DIV)
        pool_check_box = wait_until_located(self.driver, *self.POOL_CHECK_BOX)
        self.driver.execute_script('document.getElementsByName("Pool")[0].click()')

        show_filter_btn = self.driver.find_element(*self.SHOW_FILTER_RESULT_BTN)
        click(show_filter_btn)
        return self

    # Returns bedroom count of each property on search page.
    def get_bedroom_count_result(self):
        properties_bedroom_count = []
        wait_until_located(self.driver, *self.RESULT_DIV)

        # Waiting for first property's DOM object to update (after changing search filter)
        search_results = self.driver.find_elements(*self.PROPERTY_DIVS)
        try:
            wait_until_refresh(self.driver, search_results[0], timeout=30)
        except:
            pass

        # Getting updated elements from document
        wait_until_located(self.driver, *self.PROPERTY_DIVS)
        search_results = self.driver.find_elements(*self.PROPERTY_DIVS)
        for result in search_results:
            text: str = result.text
            if "bedrooms" in text:
                no_beds_str = text.split('·')[1][1:3]
                properties_bedroom_count.append(int(no_beds_str))
        return properties_bedroom_count

    def is_there_pool_in_first_property(self):
        first_property = self.driver.find_elements(*self.PROPERTY_CLICKABLE_DIVS)[0]
        click(first_property)
        self.driver.switch_to.window(self.driver.window_handles[1])

        amenities_list_btn = wait_until_located(self.driver, *self.AMENITIES_DIV).find_elements_by_tag_name("a")[0]
        click(amenities_list_btn)

        amenities_list = wait_until_located(self.driver, *self.AMENITIES_LIST).get_attribute('innerText')
        amenities_list.replace("\n", "").replace("\r", "")
        if "Pool" in amenities_list:
            return True
        return False
