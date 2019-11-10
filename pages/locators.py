from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
	BASKET_AND_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
