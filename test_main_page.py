from .pages.main_page import MainPage


# запуск тестов через pytest -v --tb=line test_main_page.py
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 5)
    page.open()
    page.go_to_login_page()


def test_should_be_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link, 5)
    page.open()
    page.should_be_login_link()
