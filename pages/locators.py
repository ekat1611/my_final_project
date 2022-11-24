from selenium.webdriver.common.by import By


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