from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY, timeout=1), \
            'There are no products in the basket'

    def should_be_message_about_empty_basket_is_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE), \
            'Message about empty basket is not presented'
