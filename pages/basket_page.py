from .base_page import BasePage
from .locators import BasketPageLocators


# методы расположены в алфавитном порядке
class BasketPage(BasePage):
    def find_text_element_on_the_basket_page(self, by, locator):
        return self.browser.find_element(by, locator).text

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.NOT_EMPTY_BASKET) is False, 'The basket consists items'

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET) is True, \
            'The basket is not empty'
