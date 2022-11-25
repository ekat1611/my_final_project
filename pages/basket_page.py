from .base_page import BasePage


class BasketPage(BasePage):
    def find_element_on_the_basket_page(self, by, locator):
        return self.browser.find_element(by, locator).text
