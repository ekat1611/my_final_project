from .base_page import BasePage
from .locators import LoginPageLocators


# методы в классе располагаются в алфавитном порядке
class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.go_to_login_page()
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        input_email.send_keys(email)
        input_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        input_password.send_keys(password)
        input_repeat_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD)
        input_repeat_password.send_keys(password)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        registration_submit.click()
        self.should_be_authorized_user()
        print(f"Зарегистрирован новый пользователь, логин {email}")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Login email is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Login password is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), 'Login submit is not presented'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, 'It is not a login page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), 'Registration email is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), 'Registration password is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD), 'Registration repeat password is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), 'Registration submit is not presented'