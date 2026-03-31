import pytest
from faker import Faker
from src.pages.login_page import LoginPage
from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage

fake = Faker()

@pytest.mark.fuzz
@pytest.mark.parametrize("bad_data", [
    fake.text(max_nb_chars=1000),  # Stress-test field length
    "❤️🔥🚀",  # Test Emoji/Unicode support
    "12345",  # Test Type validation
    "'; DROP TABLE users;--"  # Basic SQL Injection check
])
def test_checkout_form_resilience(driver, bad_data):
    # 1. Initialize all Page Objects
    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    # 2. Step-by-Step Navigation Flow
    login.login("standard_user", "secret_sauce")

    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    # Verify we actually have an item before proceeding
    assert cart.get_cart_item_count() > 0, "Cart is empty, cannot proceed to checkout"
    cart.click_checkout()

    # 3. The "Fuzzing" Execution
    checkout.enter_first_name(bad_data)
    checkout.enter_last_name("Tester")
    checkout.enter_postal_code(bad_data)
    checkout.click_continue()

    # 4. Resilience Validation
    # We aren't checking for "Success" here; we are checking for "Stability"
    # A 500 error means the backend crashed. A standard error message means it's safe.
    assert "Internal Server Error" not in driver.page_source
    print(f"Verified: System remained stable with input: {bad_data[:20]}...")