# test_login.py

import pytest
from selenium import webdriver
from config.config import Config

@pytest.fixture(scope="module")
def driver():
    """Set up the WebDriver and return it."""
    options = Config.get_browser_options()
    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH, options=options)
    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH, options=options)
    else:
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()

def test_login_valid_user(driver):
    """Test logging in with valid user credentials."""
    driver.find_element_by_id("user-name").send_keys(Config.USERNAME)
    driver.find_element_by_id("password").send_keys(Config.PASSWORD)
    driver.find_element_by_id("login-button").click()
    
    # Check if login is successful by verifying the presence of a logout button
    assert driver.find_element_by_id("logout_sidebar_link").is_displayed()

