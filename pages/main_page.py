from .base_page import BasePage


class MainPage(BasePage):

    # заглушка, которая вызывает конструктор класса предка BasePage и передаёт ему полученные аргументы
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
