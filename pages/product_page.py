from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
	def should_be_purchased_product(self):
		self.should_be_add_to_basket_button()
		self.add_to_basket()
		time.sleep(5)
		self.should_be_product_name()
		self.should_be_basket_and_product_price()

	def should_be_add_to_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button is not presented"

	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		button.click()
		self.solve_quiz_and_get_code()

	def should_be_product_name(self):
		assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == "The shellcoder's handbook", "Name is not true"

	def should_be_basket_and_product_price(self):
		assert self.browser.find_element(*ProductPageLocators.BASKET_AND_PRODUCT_PRICE).text == "9,99 £", "Price is not correct"


