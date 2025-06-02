from time import sleep

from pages.base_page import BasePage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


class ProductLocators:
    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")
    GO_TO_CART = (By.ID, "cartur")
    GO_TO_HOME = (By.LINK_TEXT, "Home ")
    GET_PRODUCT_PRICE = (By.XPATH, "/html/body/div[5]/div/div[2]/h3")

class ProductPage(BasePage):
    def add_to_cart(self):
        # Waits for the 'Add to cart' link to be clickable and clicks it
        el = self.wait_5s.until(EC.element_to_be_clickable(ProductLocators.ADD_TO_CART))
        el.click()

    def confirm_alert(self):
        # Confirm alert (clicks OK)
        alert = self.wait_5s.until(EC.alert_is_present())
        alert.accept()

    def go_to_cart(self):
        # Click the cart button and return CartPage instance
        self.driver.find_element(*ProductLocators.GO_TO_CART).click()
        return CartPage(self.driver)

    def go_to_home(self):
        # Click the home link and return HomePage instance
        self.driver.find_element(*ProductLocators.GO_TO_HOME).click()
        return HomePage(self.driver)

    def get_product_price(self):
        sleep(4)  # Wait for the price to be visible/stabilized
        text_and_price = self.driver.find_element(*ProductLocators.GET_PRODUCT_PRICE).text
        # Extract digits from the price text and convert to int
        price = ''.join(filter(str.isdigit, text_and_price))
        price = int(price)  # +0 is redundant so omitted
        return price