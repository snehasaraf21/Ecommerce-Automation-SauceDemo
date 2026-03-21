from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    SUCCESS_MSG=(By.CLASS_NAME,"complete-header")

    def enter_first_name(self,first_name):
        self.send_keys(CheckoutPage.FIRST_NAME,first_name)

    def enter_last_name(self,last_name):
        self.send_keys(CheckoutPage.LAST_NAME,last_name)

    def enter_postal_code(self,postal_code):
        self.send_keys(CheckoutPage.POSTAL_CODE,postal_code)

    def click_continue(self):
        self.click(CheckoutPage.CONTINUE_BTN)

    def click_finish(self):
        self.click(CheckoutPage.FINISH_BTN)

    def complete_checkout(self,first_name,last_name,postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
        self.click_finish()


    def get_success_message(self):
        return self.get_text(CheckoutPage.SUCCESS_MSG)
