from pages.home_page import HomePage
from tests.base_test import BaseTest
from pages.cart_page import CartPage
from time import sleep
import random

# Number of phones to add to the cart (random from 1 to 4)
number_of_phones = random.randint(1, 4)

# List of available products on the home page
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

class AddToCartTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Additional precondition – navigate to the home page
        self.home_page = HomePage(self.driver)

    def test_add_samsung_to_cart(self):
        total_price = 0

        for i in range(number_of_phones):
            # Select a random phone from the list
            phone_from_list = random.randint(0, 7)

            # Click on the product to view its page
            self.product_page = self.home_page.click_product(list_products_on_home_page[phone_from_list])

            # Add the product's price to the total
            total_price += self.product_page.get_product_price()

            # Add product to cart
            self.product_page.add_to_cart()
            sleep(2)  # Wait for alert or UI action

            # Confirm the alert that appears after adding to cart
            self.product_page.confirm_alert()
            sleep(2)

            # Go back to the home page (twice if needed)
            self.driver.back()
            self.driver.back()

        # Go to the cart
        self.home_page.click_cart()

        # Print total product price
        print("Sumaryczna cena produktów: " + str(total_price))

        # Go to cart and print Total Price
        self.cart_page = CartPage(self.driver)
        print("Cena z koszyka: " + self.cart_page.get_total_price_text())
        sleep(2)

        # Validate that the total of added products matches the cart total
        self.assertEqual(int(self.cart_page.get_total_price_text()), total_price)