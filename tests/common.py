from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def wait_until_located(driver, by, value, timeout=10):
    element_present = EC.presence_of_element_located((by, value))
    WebDriverWait(driver, timeout).until(element_present)


def move_to(driver, xpath):
    element_to_hover_over = driver.find_element_by_xpath(xpath)
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()
