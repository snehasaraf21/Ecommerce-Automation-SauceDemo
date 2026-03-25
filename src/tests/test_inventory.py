import pytest
import allure
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage

@allure.feature("Inventory")
def test_add_to_cart(driver):
    login = LoginPage(driver)
    inventory=InventoryPage(driver)

    login.login("standard_user","secret_sauce")
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count()=="1"





