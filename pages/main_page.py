from .base_page import BasePage
from .basket_page import BasketPage
from .locators import MainPageLocators


class MainPage(BasePage):

    # заглушка, которая вызывает конструктор класса предка BasePage и передаёт ему полученные аргументы
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
