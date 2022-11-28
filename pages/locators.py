from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name = \'login_submit\']')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, '[name = \'registration_submit\']')


class ProductPageLocators:
    BUTTON_ADD_TO_THE_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_NAME_IN_THE_BASKET = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner strong")
    ITEM_PRICE_IN_THE_BASKET = (By.CSS_SELECTOR, ".alertinner  p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")


class BasketPageLocators:
    NOT_EMPTY_BASKET = (By.CSS_SELECTOR, '.basket_summary')
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner>p')