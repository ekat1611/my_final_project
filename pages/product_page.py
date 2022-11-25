from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def find_element_on_the_product_page(self, by, locator):
        return self.browser.find_element(by, locator).text

    def add_item_to_the_basket(self):
        item_price = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_PRICE)
        item_name = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_NAME)
        button_add_to_the_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_THE_BASKET)
        button_add_to_the_basket.click()
        self.solve_quiz_and_get_code()
        return item_price, item_name

