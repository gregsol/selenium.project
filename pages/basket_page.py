from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), \
            'There are products in a basket'

    def correct_copy_for_empty_basket(self):
        copy = self.browser.find_element(*BasketPageLocators.BASKET_CONTAINER).text
        assert copy == 'Your basket is empty. Continue shopping', \
            'Wrong copy for an empty basket'