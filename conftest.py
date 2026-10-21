import pytest
from selenium import webdriver


@pytest.fixture
def driver_fix():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument("--guest")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

