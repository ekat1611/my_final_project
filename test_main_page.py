import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


# запуск тестов через pytest -v --tb=line test_main_page.py
def test_check_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 5)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url, 5)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link, 5)
    page.open()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.go_to_the_basket_page()
    page_basket.should_be_empty_basket()
    page_basket.should_be_text_about_empty_basket()
