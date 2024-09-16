from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ITEM = (By.CLASS_NAME, 'inventory_item')
    CART_BTN = (By.CLASS_NAME, 'shopping_cart_link')

    def add_item_to_cart(self, item_index=0):
        items = self.driver.find_elements(*self.ITEM)
        items[item_index].find_element(By.TAG_NAME, 'button').click()

    def go_to_cart(self):
        self.find_element(self.CART_BTN).click()
