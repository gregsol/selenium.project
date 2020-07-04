from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_should_be_added(self):
        item_added = self.browser.find_element(*ProductPageLocators.ITEM_ADDED).text
        title = self.browser.find_element(*ProductPageLocators.TITLE).text
        message = title + ' has been added to your basket.'
        assert message == item_added, 'Item has not been added to the basket or message is incorrect'

    def price_updated(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        message = 'Your basket total is now ' + price
        assert message == price_in_basket, 'Price was not updated or message is incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED), \
            "Success message is presented, but should not be"

    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_ADDED), \
            "Success message didn't disappear"