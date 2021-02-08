from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(1).alert-safe > .alertinner strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages :nth-child(3).alert-safe > .alertinner  strong")
    PRODUCT_NAME = "Coders at Work"
    PRODUCT_PRICE = "£19.99"