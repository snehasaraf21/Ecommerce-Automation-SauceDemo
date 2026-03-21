import pytest
import allure
from src.pages.login_page import LoginPage


@allure.feature("login")
def test_valid_login(driver):
    login = LoginPage(driver)

    login.login("standard_user","secret_sauce")
    assert "inventory" in driver.current_url

@allure.feature("login")
def test_invalid_login(driver):
    login = LoginPage(driver)

    login.login("wrong _user", "wrong_pass")
    assert "do not match" in login.get_error_message()
