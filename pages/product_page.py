from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def should_be_text_message_is_correct(self):
        basket_message = self.browser.find_element(*ProductPageLocators.TEXT_IN_ADD_BASKET_MESSAGE).text
        text_product_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert text_product_name == basket_message, 'Name of product is incorrect'

    def should_be_price_basket_is_correct(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_ADD_BASKET_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_product == price_basket, 'Price of product is incorrect'