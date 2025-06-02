from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # to check if elements are clickable

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SignUpLocators:
    SIGN_UP_BUTTON = (By.XPATH, '//button[@onclick="register()"]')
    SIGN_UP_USERNAME = (By.ID, 'sign-username')
    SIGN_UP_PASSWORD = (By.ID, 'sign-password')


class SignUpPage(BasePage):
    """
    Sign Up page object
    """
    def click_sign_up(self):
        # Waits 5 seconds for sign-up button and clicks it
        el = self.driver.find_element(*SignUpLocators.SIGN_UP_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()
        self.wait_5s.until(EC.alert_is_present()).accept()


    def get_alert_message(self):
        # Wait 5 seconds for alert and returns its text
        self.wait_5s.until(EC.alert_is_present())
        return self.alert.text

    def confirm_alert(self):
        # Confirm alert after it shows up
        self.alert.accept()

    def enter_username(self, username):
        self.driver.find_element(*SignUpLocators.SIGN_UP_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*SignUpLocators.SIGN_UP_PASSWORD).send_keys(password)

    def _verife_page(self):
        # Wait for username and password fields to be visible
        self.wait_5s.until(EC.visibility_of_element_located(SignUpLocators.SIGN_UP_USERNAME))
        self.wait_5s.until(EC.visibility_of_element_located(SignUpLocators.SIGN_UP_PASSWORD))
