import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome(r"chromedriver.exe")
    driver.maximize_window()
    # By implicitly waiting (for elements to appear) before each call resolves time.sleep() issue
    driver.implicitly_wait(10)

    yield driver

    driver.quit()

