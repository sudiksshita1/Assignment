from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, 'checkout')

    def proceed_to_checkout(self):
        self.find_element(self.CHECKOUT_BTN).click()
