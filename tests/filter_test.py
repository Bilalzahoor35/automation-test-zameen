import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.common import wait_until_located, move_to
from .test_search import landing_page_searching_param


def filter_search_criteria_test(driver, prev_success):
    print("Running: Filter Search criteria test.")
    if not prev_success:
        landing_page_searching_param(driver)
    wait_until_located(driver, By.CLASS_NAME, '_fhph4u')
    filter_button = driver.find_element_by_id("menuItemButton-dynamicMoreFilters").find_elements_by_tag_name("button")[
        0]
    filter_button.send_keys(Keys.RETURN)

    wait_until_located(driver, By.CSS_SELECTOR,
                       '[data-testid="filterItem-rooms_and_beds-stepper-min_bedrooms-0-increase-button"]')
    time.sleep(2)

    bed_rooms_btn = driver.find_element_by_css_selector(
        '[data-testid="filterItem-rooms_and_beds-stepper-min_bedrooms-0-increase-button"]')
    bed_rooms_btn.send_keys(Keys.RETURN)
    bed_rooms_btn.send_keys(Keys.RETURN)
    bed_rooms_btn.send_keys(Keys.RETURN)
    bed_rooms_btn.send_keys(Keys.RETURN)
    bed_rooms_btn.send_keys(Keys.RETURN)

    move_to(driver, '//*[@name="Apartment"]')
    time.sleep(2)
    driver.execute_script('document.getElementsByName("Pool")[0].click()')

    show_filter_btn = driver.find_element_by_css_selector('[data-testid="more-filters-modal-submit-button"]')
    show_filter_btn.send_keys(Keys.RETURN)

    time.sleep(5)
    search_results = driver.find_elements_by_xpath('//*[@class="_kqh46o"]')
    for result in search_results:
        text: str = result.text
        if "bedrooms" in text:
            no_beds_str = text.split('·')[1][1:3]
            try:
                assert int(no_beds_str) >= 5
            except AssertionError:
                print("Bedroom filter criteria test failed.")
                return
    print("     Bedroom filter criteria test passed.")
    if not pool_in_first_property(driver):
        print("Pool filter criteria test failed.")
    print("     Pool filter criteria test passed.")

    print("Passed: Filter Search criteria test.")
    time.sleep(1)


def pool_in_first_property(driver):
    temp = "https://www.airbnb.com/s/Rome--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&query=Rome%2C%20Italy&place_id=ChIJw0rXGxGKJRMRAIE4sppPCQM&adults=2&children=1&source=structured_search_input_header&search_type=autocomplete_click"
    driver.get(temp)
    property = driver.find_elements_by_xpath('//*[@class="_gjfol0"]')[0]
    property.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    wait_until_located(driver, By.CLASS_NAME, '_1tv4hg3')

    amenities_btn = driver.find_element_by_class_name('_1tv4hg3').find_elements_by_tag_name("a")[0]
    amenities_btn.send_keys(Keys.RETURN)

    time.sleep(4)
    wait_until_located(driver, By.CLASS_NAME, '_1seuw5go')
    amenities_list = driver.find_element_by_class_name("_1seuw5go").get_attribute('innerText')
    if "Pool" in amenities_list:
        return True
    return False


def run_filter_criteria_test(driver, prev_success):
    try:
        filter_search_criteria_test(driver, prev_success)
        return True
    except:
        return False
