from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, 'login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[value="Add to basket"]')
    ITEM_ADDED = (By.CLASS_NAME, 'alertinner')
    TITLE = (By.CSS_SELECTOR, 'div.product_main h1')
    PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '#messages :nth-child(3) > .alertinner > p')
