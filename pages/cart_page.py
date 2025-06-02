from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Cart page locators
class CartLocators:
    DELETE_BUTTON = (By.LINK_TEXT, "Delete")
    PRODUCT_TABLE = (By.ID, 'tbodyid')
    TOTAL_PRICE = (By.ID, 'totalp')
    FIRST_ITEM_IN_TABLE = (By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[2]")

class CartPage(BasePage):

    # Delete the first product from the cart
    def click_delete(self):
        el = self.driver.find_element(*CartLocators.DELETE_BUTTON)
        self.wait_5s.until(EC.element_to_be_clickable(el))
        el.click()

    # Get total price displayed in the cart
    def get_total_price_text(self):
        price = self.wait_5s.until(
            EC.visibility_of_element_located(CartLocators.TOTAL_PRICE)
        )
        return price.text

    # Count all items (rows) present in the cart table
    def count_table_rows(self):
        table = self.wait_5s.until(
            EC.presence_of_element_located(CartLocators.PRODUCT_TABLE)
        )
        sleep(2)  # Wait for table rows to stabilize
        rows = table.find_elements(By.TAG_NAME, "tr")
        return len(rows)

    # Get the name of the first item listed in the cart
    def get_first_item_name(self):
        item_name = self.driver.find_element(*CartLocators.FIRST_ITEM_IN_TABLE).text
        return item_name
