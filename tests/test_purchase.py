import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup")
class TestPurchase:
    def test_purchase_flow(self):
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)

        inventory_page.open("inventory.html")
        inventory_page.add_item_to_cart()
        inventory_page.go_to_cart()

        cart_page.proceed_to_checkout()

        checkout_page.fill_checkout_info("John", "Doe", "12345")
        assert "checkout-step-two" in self.driver.current_url


