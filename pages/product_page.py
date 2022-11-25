from .base_page import BasePage
from .locators import ProductPageLocators
from time import sleep


class ProductPage(BasePage):
    def find_element_on_the_product_page(self, by, locator):
        return self.browser.find_element(by, locator).text

    def add_item_to_the_basket(self):
        button_add_to_the_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_THE_BASKET)
        button_add_to_the_basket.click()
        self.solve_quiz_and_get_code()
        item_price = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_PRICE)
        item_name = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_NAME)
        item_price_in_the_basket = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_PRICE_IN_THE_BASKET)
        item_name_in_the_basket = self.find_element_on_the_product_page(*ProductPageLocators.ITEM_NAME_IN_THE_BASKET)
        assert item_price_in_the_basket == item_price, f'Стоимость товара в корзине не соответствует цене товара, ' \
                                                       f'ожидалось значение: {item_price}, получено ' \
                                                       f'{item_price_in_the_basket}'
        assert item_name_in_the_basket == item_name, f'Наименование товара в корзине не соответствует названию товара, ' \
                                                     f'ожидалось значение: {item_name}, получено ' \
                                                     f'{item_name_in_the_basket}'

