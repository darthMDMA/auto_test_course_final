from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import AddProductLocators
from selenium.common.exceptions import NoAlertPresentException
import time
import math


class ProductPage(BasePage):
    def check_all_asserts(self):
        self.add_product_to_trash()
        self.alert_of_added_product()
        self.basket_cost_mesage()

    def add_product_to_trash(self):
        add_product_button = self.browser.find_element(*AddProductLocators.ADD_PRODUCT)
        add_product_button.click()
        self.solve_quiz_and_get_code()
        assert add_product_button, "кнопка не нажата, товар не добавлен"

    def alert_of_added_product(self):
        time.sleep(5)
        product_name = self.browser.find_element(By.TAG_NAME, "h1" ).text
        prodcut_alert = self.browser.find_element(By.XPATH, f'//strong[contains(text(), "{product_name}")]').text
        assert prodcut_alert == product_name, "сообщение о добавленном товаре не найдено"


    def basket_cost_mesage(self):
        price = self.browser.find_element(*AddProductLocators.PRICE).text
        message = self.browser.find_element(By.XPATH, f'//strong[contains(text(), "{price}")]').text
        assert price == message, "сообщение со стоимостью корзины не найдено либо цена не совпадает"

    def guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert not self.is_not_element_present(*AddProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def guest_cant_see_success_message(self):
        assert self.is_not_element_present(*AddProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert not self.is_disappeared(*AddProductLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"



    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        time.sleep(1)
        alert.send_keys(answer)
        time.sleep(1)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
