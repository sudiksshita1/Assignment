from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.find_element(self.FIRST_NAME).send_keys(first_name)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.POSTAL_CODE).send_keys(postal_code)
        self.find_element(self.CONTINUE_BTN).click()
