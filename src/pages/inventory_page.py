from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BACKPACK = (By.ID,"add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME,"shopping_cart_link")
    CART_COUNT = (By.CLASS_NAME,"shopping_cart_badge")



    def add_backpack_to_cart(self):
        self.click(InventoryPage.ADD_TO_CART_BACKPACK)


    def go_to_cart(self):
        self.click(InventoryPage.CART_ICON)

    def get_cart_count(self):
        return self.get_text(InventoryPage.CART_COUNT)
