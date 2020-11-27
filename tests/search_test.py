import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .common import wait_until_located, move_to


def landing_page_searching_param(driver):
    driver.get("https://www.airbnb.com/")
    wait_until_located(driver, By.ID, 'bigsearch-query-detached-query')

    search_box = driver.find_element_by_id("bigsearch-query-detached-query")
    search_box.send_keys("Rome, Italy")

    guest_button = driver.find_element_by_css_selector('[data-testid="structured-search-input-field-guests-button"]')
    guest_button.send_keys(Keys.RETURN)

    time.sleep(1)

    adult_button = driver.find_element_by_css_selector('[data-testid="stepper-adults-increase-button"]')
    adult_button.send_keys(Keys.RETURN)
    adult_button.send_keys(Keys.RETURN)

    child_button = driver.find_element_by_css_selector('[data-testid="stepper-children-increase-button"]')
    child_button.send_keys(Keys.RETURN)

    search_button = driver.find_element_by_css_selector('[data-testid="structured-search-input-search-button"]')
    search_button.send_keys(Keys.RETURN)
    time.sleep(5)


def initial_search_criteria_test(driver):
    print("Running: Search criteria test.")
    wait_until_located(driver, By.CLASS_NAME, '_fhph4u')
    search_results = driver.find_elements_by_xpath('//*[@class="_kqh46o"]')
    for result in search_results:
        text: str = result.text
        if "guests" in text:
            try:
                assert int(text[0:2]) >= 3
            except AssertionError:
                print("Search criteria test failed.")
                return
    print("Passed: Search criteria test.")
    time.sleep(1)
    return driver


def run_search_criteria_test(driver):
    try:
        landing_page_searching_param(driver)
        initial_search_criteria_test(driver)
        return True
    except:
        return False
