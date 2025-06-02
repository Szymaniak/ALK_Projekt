from tests.base_test import BaseTest
from time import sleep

class LoginTest(BaseTest):
    def setUp(self):
        super().setUp()
        # Additional precondition – navigate to the login page
        self.login_page = self.home_page.click_log_in()

    def testEmptyLogin(self):
        # Do not enter anything
        # Click login
        self.login_page.click_log_in()

        # Verify alert message
        self.assertEqual(self.login_page.get_alert_message(), "Please fill out Username and Password.")

        # Confirm alert
        sleep(2)
        self.login_page.confirm_alert()

    def testValidLogin(self):
        username = "tester_alk"

        # Enter username
        self.login_page.enter_username("tester_alk")
        sleep(3)

        # Enter password
        self.login_page.enter_password("haslo")

        # Click Log in
        self.login_page.click_log_in()

        # Check if "Welcome tester_alk" appears on the page
        self.assertEqual(f"Welcome {username}", self.home_page.get_welcome_user_name_text())

        # Check if logout can be clicked
        self.home_page.click_log_out()
        pass


