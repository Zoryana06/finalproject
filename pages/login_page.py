from .base_page import BasePage
from .locators import LoginPageLocators
from random import randint
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "'/login' is not current url"  

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        time.sleep(1)
        email_example = str(randint(10000, 99999)) + "@fakemail.com"
        password_example = "Qwerty" + str (randint(10000, 99999))

        self.email = self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email_example)
        self.password = self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password_example)
        self.password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD).send_keys(password_example)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
