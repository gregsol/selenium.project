from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_IN_HEADER = (By.CSS_SELECTOR, 'div.basket-mini span.btn-group a.btn-default')

class MainPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')

class BasketPageLocators():
    BASKET_CONTAINER = (By.ID, 'content_inner')
    BASKET_TOTAL = (By.CSS_SELECTOR, 'h3.price_color')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    ITEM_ADDED = (By.CLASS_NAME, 'alertinner')
    TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) > .alertinner > p')
