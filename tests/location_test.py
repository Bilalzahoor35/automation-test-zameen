from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from pages.common import wait_until_located
from .test_search import run_search_criteria_test


def run_location_test(driver):
    print("Running: Location Map test.")
    try:
        run_search_criteria_test(driver)
        wait_until_located(driver, By.CLASS_NAME, '_fhph4u')
        time.sleep(5)
        properties = driver.find_elements_by_xpath('//*[@class="_kqh46o"]')
        action = ActionChains(driver)
        action.move_to_element(properties[0]).perform()
    except:
        print("Failed: Location Map test.")
    print("Passed: Location Map test.")
