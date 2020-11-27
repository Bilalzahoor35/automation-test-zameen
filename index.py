import time

from selenium import webdriver
from tests.search_test import run_search_criteria_test
from tests.filter_test import run_filter_criteria_test
from tests.location_test import run_location_test

driver = webdriver.Chrome(r"chromedriver.exe")
driver.maximize_window()
success = run_search_criteria_test(driver)
run_filter_criteria_test(driver, success)
run_location_test(driver)

time.sleep(10)
driver.close()
