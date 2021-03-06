from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.product_main .price_color')
    TEXT_IN_ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    PRICE_IN_ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, '.alert .alert-safe .alert-noicon .alert-info  .fade in')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_BASKET = (By.CSS_SELECTOR, '.btn-group')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_SUMMARY = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner')

