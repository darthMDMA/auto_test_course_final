from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.NAME, "registration-email")
    PASSWORD1 = (By.NAME, "registration-password1")
    PASSWORD2 = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")

class AddProductLocators:
    ADD_PRODUCT = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE = (By.XPATH, '//p[@class="price_color"]')
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert alert-safe alert-noicon alert-success  fade in")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.PARTIAL_LINK_TEXT, "basket")
    CHECKOUT_BUTTON = (By.PARTIAL_LINK_TEXT, "checkout")
    EMPTY_BASkET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")