
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import re


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self,locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def click_fuzzy_button(self, text_pattern):
        """Finds a button using a regex pattern to handle 'fuzzy' text matching."""
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for btn in buttons:
            # Matches text ignoring case and minor variations
            if re.search(text_pattern, btn.text, re.IGNORECASE):
                btn.click()
                return
        raise Exception(f"Fuzzy Button with pattern '{text_pattern}' not found!")