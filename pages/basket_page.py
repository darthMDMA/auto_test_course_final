from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET), "Basket link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET)
        link.click()

    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.CHECKOUT_BUTTON), "товар есть в корзине"

    def guest_can_see_empty_basket_text(self):
        self.is_element_present(*BasePageLocators.EMPTY_BASkET_MESSAGE), "нет сообщения, что корзина пуста"

