from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_until_located(driver, by, value, timeout=60):
    element_present = EC.presence_of_element_located((by, value))
    return WebDriverWait(driver, timeout).until(element_present)


def wait_until_refresh(driver, element, timeout=30):
    return WebDriverWait(driver, timeout).until(EC.staleness_of(element))


def move_to(driver, by, value):
    element_to_hover_over = driver.find_element(by, value)
    hover = ActionChains(driver).move_to_element(element_to_hover_over)
    hover.perform()


def move_to_element(driver, element):
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()


def click(btn, times=1):
    for i in range(times):
        btn.send_keys(Keys.RETURN)
