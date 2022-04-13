import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "123"
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_text_message_is_correct()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_empty_basket()
    page.should_be_message_about_empty_basket_is_present()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, link)
    page.should_be_empty_basket()
    page.should_be_message_about_empty_basket_is_present()




