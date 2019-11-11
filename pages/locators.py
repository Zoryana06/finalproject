from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
	CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators():
	BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner > strong")
	BASKET_AND_PRODUCT_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong")
	TITLE = (By.CSS_SELECTOR, "div.product_main > h1")
	SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success']/div[@class='alertinner']")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	VIEW_BASKET = (By.XPATH, "//a[contains(text(), 'View basket')]")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
	EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")