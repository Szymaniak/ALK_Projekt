from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.signup_page import SignUpPage
from pages.cart_page import CartPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC # do sprawdzania czy elemtnty są klikalne

class HomePageLocators:

    # Home page locators
    LOG_IN_A = (By.ID, "login2")
    LOG_OUT_A = (By.ID, "logout2")
    SIGN_UP_A = (By.ID, "signin2")
    SAMSUNG_GALAXY_S6 = (By.LINK_TEXT, "Samsung galaxy s6")
    GO_TO_CART = (By.ID, "cartur")
    LOGGED_USER_NAME = (By.ID, "nameofuser")

    pass

class HomePage(BasePage):
    def click_log_in(self):

        # Find button log in and click it
        self.driver.find_element(*HomePageLocators.LOG_IN_A).click()

        # return login page
        return LoginPage(self.driver)

    def click_log_out(self):

        # Find button log in and click it
        self.driver.find_element(*HomePageLocators.LOG_OUT_A).click()

    def click_sign_up(self):

        # Find button sign up and click it
        self.driver.find_element(*HomePageLocators.SIGN_UP_A).click()
        return SignUpPage(self.driver)

    def click_cart(self):

        # Click and return Cart page
        self.driver.find_element(*HomePageLocators.GO_TO_CART).click()
        return CartPage(self.driver)

    def click_product(self,phone_name):

        # import inside of function to avoid infinite loop, during one of the tests
        from pages.product_page import ProductPage

        # Wait till phone list on home page will be loaded
        self.wait_5s.until(EC.text_to_be_present_in_element((By.LINK_TEXT, phone_name), phone_name))

        # Click and return product page
        self.driver.find_element(*(By.LINK_TEXT, phone_name)).click()
        return ProductPage(self.driver)

    def get_welcome_user_name_text(self):

        #gets Welcome <USERNAME> message from top right of the page
        self.wait_5s.until(EC.text_to_be_present_in_element(HomePageLocators.LOGGED_USER_NAME, "Welcome"))
        return self.driver.find_element(*HomePageLocators.LOGGED_USER_NAME).text