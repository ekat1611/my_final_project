from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def find_element_on_the_basket_page(self, by, locator):
        return self.browser.find_element(by, locator).text

    def check_add_item_to_the_basket(self, item_price, item_name):
        item_price_in_the_basket = self.find_element_on_the_basket_page(*BasketPageLocators.ITEM_PRICE_IN_THE_BASKET)
        item_name_in_the_basket = self.find_element_on_the_basket_page(*BasketPageLocators.ITEM_NAME_IN_THE_BASKET)
        assert item_price_in_the_basket == item_price, f'Стоимость товара в корзине не соответствует цене товара, ' \
                                                       f'ожидалось значение: {item_price}, получено ' \
                                                       f'{item_price_in_the_basket}'
        assert item_name_in_the_basket == item_name, f'Наименование товара в корзине не соответствует названию товара, ' \
                                                     f'ожидалось значение: {item_name}, получено ' \
                                                     f'{item_name_in_the_basket}'
