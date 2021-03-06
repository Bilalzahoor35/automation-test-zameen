import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome(r"chromedriver.exe")
    driver.maximize_window()
    # By implicitly waiting (for elements to appear) after each call resolves time.sleep() issue
    driver.implicitly_wait(60)

    yield driver

    driver.quit()
