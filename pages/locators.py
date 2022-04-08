from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    TEXT_IN_ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PRICE_IN_ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert .alert-safe .alert-noicon .alert-info  .fade in')
