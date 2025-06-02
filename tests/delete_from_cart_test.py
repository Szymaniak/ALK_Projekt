from tests.base_test import BaseTest
from pages.cart_page import CartPage
from time import sleep
from datetime import datetime
import os

# Test: Add Samsung Galaxy S6 to cart and remove it

class AddToCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Additional precondition - navigate to the product page

        self.product_page = self.home_page.click_product("Samsung galaxy s6")

    def test_add_samsung_to_cart(self):
        # Add phone to cart
        self.product_page.add_to_cart()

        # Confirm alert about item being added to cart
        self.product_page.confirm_alert()

        # Go to cart
        self.product_page.go_to_cart()
        self.cart_page = CartPage(self.driver)


        # Folder and creation if folder does not exist
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)

        # Get date and time and combine it into path to save screenshots
        date = datetime.now().strftime("%Y%m%d_%H%M")
        filepath = os.path.join(folder, date)

        # Print how many items are in the cart and save screenshot of cart
        print("Number of products in cart before removal: ", self.cart_page.count_table_rows())
        self.driver.save_screenshot(filepath+"_screenshot_before_removal.png")

        # Remove item from cart
        self.cart_page.click_delete()
        sleep(2)

        # Print how many items are in the cart after removal and save screenshot of cart
        self.driver.save_screenshot(filepath+'_screenshot_after_removal.png')
        print("Number of products in cart after removal: ", self.cart_page.count_table_rows())
        sleep(2)

