from tests.base_test import BaseTest
from time import sleep
from faker import Faker
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # to check if elements are clickable
from selenium.webdriver.common.keys import Keys

# Create registration data for the user using the Faker library
fake = Faker()
username = fake.email()
characters = string.ascii_letters + string.digits
password = ''.join(random.choices(characters, k=10))

class SignUpTest(BaseTest):
    def setUp(self):
        super().setUp()

    # Create user
    def testValidSignUp(self):

        # Open sign up window
        self.signup_page = self.home_page.click_sign_up()

        # Enter username
        self.signup_page.enter_username(username)
        sleep(3)

        # Enter password
        self.signup_page.enter_password(password)

        # Click Sign up
        self.signup_page.click_sign_up()

    # Log in with the created user
    def testValidlogIn(self):

        # Open log in window
        self.login_page = self.home_page.click_log_in()

        # Enter username
        self.login_page.enter_username(username)
        sleep(3)

        # Enter password
        self.login_page.enter_password(password)

        # Click Log in
        self.login_page.click_log_in()

        # Verify if the user is logged in with the previously registered username
        self.assertEqual(f"Welcome {username}", self.home_page.get_welcome_user_name_text())
        pass