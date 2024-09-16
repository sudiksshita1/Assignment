from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login-button')

    def login(self, username, password):
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.LOGIN_BTN).click()
