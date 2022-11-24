from .pages.main_page import MainPage
from .pages.login_page import LoginPage


# запуск тестов через pytest -v --tb=line test_main_page.py
def test_check_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 5)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url, 5)
    login_page.should_be_login_page()

