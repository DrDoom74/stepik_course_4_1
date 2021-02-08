from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from time import sleep

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def product_should_be_in_basket(self):
        self.solve_quiz_and_get_code()

    def should_be_the_same_product(self):
        expected_product_name = ProductPageLocators.PRODUCT_NAME
        product_message = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE)
        prod_val = product_message.text
        assert expected_product_name == prod_val, \
            f"The product name {prod_val} is not {expected_product_name}"

    def should_be_the_same_price(self):
        expected_product_price = ProductPageLocators.PRODUCT_PRICE
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        price_val = price_message.text
        #print(price_val)
        assert expected_product_price == price_val, \
            f"The price {price_val} is differ than {expected_product_price}"
