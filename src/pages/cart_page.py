from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage



class CartPage(BasePage):
     CHECKOUT_BTN = (By.ID, "checkout")
     CART_ITEM = (By.CLASS_NAME, "inventory_item_name")


     def click_checkout(self):
         self.click(CartPage.CHECKOUT_BTN)



     def get_cart_item_count(self):
        return len(self.driver.find_elements(*CartPage.CART_ITEM))
