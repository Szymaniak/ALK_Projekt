from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # used to check if elements are clickable

# Login page locators
class LoginPageLocators:
    LOG_IN_BUTTON = (By.XPATH, '//button[@onclick="logIn()"]')
    LOG_IN_USERNAME = (By.ID, 'loginusername')
    LOG_IN_PASSWORD = (By.ID, 'loginpassword')


class LoginPage(BasePage):

    def click_log_in(self):
        # Waits up to 5 seconds for the login button to be clickable, then clicks it
        el = self.driver.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()

    def get_alert_message(self):
        # Waits up to 5 seconds for the alert to be present and returns its text
        self.wait_5s.until(EC.alert_is_present())
        return self.alert.text

    def confirm_alert(self):
        # Accepts the alert
        self.alert.accept()

    def enter_username(self, username):
        # Enters the provided username
        self.driver.find_element(*LoginPageLocators.LOG_IN_USERNAME).send_keys(username)

    def enter_password(self, password):
        # Enters the provided password
        self.driver.find_element(*LoginPageLocators.LOG_IN_PASSWORD).send_keys(password)

    def _verife_page(self):
        # Waits for the login page username and password fields to be visible
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.LOG_IN_USERNAME))
        self.wait_5s.until(EC.visibility_of_element_located(LoginPageLocators.LOG_IN_PASSWORD))
