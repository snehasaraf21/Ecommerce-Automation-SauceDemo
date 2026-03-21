import allure
import time
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.checkout_page import CheckoutPage
from src.pages.cart_page import CartPage


@allure.feature("Checkout")
def test_complete_checkout(driver):
    login=LoginPage(driver)
    inventory=InventoryPage(driver)
    cart=CartPage(driver)
    checkout=CheckoutPage(driver)

    login.login("standard_user","secret_sauce")


    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"

    inventory.go_to_cart()
    cart.click_checkout()


    checkout.complete_checkout("John","Doe","12345")

    assert "Thank you for your order!" in checkout.get_success_message()