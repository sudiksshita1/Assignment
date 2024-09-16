import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()
