from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "в url не содержится login"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "форма входа не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "форма регистрации не найдена"

    def register_new_user(self, email, password):
        e = self.browser.find_element(*LoginPageLocators.EMAIL)
        e.send_keys(email)
        p1 = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        p1.send_keys(password)
        p2 = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        p2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        reg_button.click()