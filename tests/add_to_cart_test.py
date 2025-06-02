from tests.base_test import BaseTest
from pages.cart_page import CartPage
from time import sleep
import random

# Test: Check if a product is added to the cart after clicking "Add to cart"

# List of phones displayed on the home page
list_products_on_home_page = [
    "Samsung galaxy s6",
    "Nokia lumia 1520",
    "Nexus 6",
    "Samsung galaxy s7",
    "Iphone 6 32gb",
    "Sony xperia z5",
    "HTC One M9",
    "Sony vaio i5"
]

# Randomly select one phone from the list
phone_from_list = random.randint(0, 7)


class AddToCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Navigate to the selected product page
        self.product_page = self.home_page.click_product(list_products_on_home_page[phone_from_list])

    def test_add_samsung_to_cart(self):
        # Add the product to the cart
        self.product_page.add_to_cart()

        # Confirm the alert
        self.product_page.confirm_alert()

        # Navigate to the cart page
        self.product_page.go_to_cart()
        self.cart_page = CartPage(self.driver)

        sleep(2)

        # Get the name of the first item in the cart
        first_item_name = self.cart_page.get_first_item_name()

        # Verify the item in the cart matches the selected product
        self.assertEqual(list_products_on_home_page[phone_from_list], first_item_name)


