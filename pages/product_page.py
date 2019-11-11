from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
	def should_be_purchased_product(self):
		self.should_be_add_to_basket_button()
		self.add_to_basket()
		self.should_be_product_name()
		self.should_be_basket_and_product_cost()
		self.should_be_name_equal_title()

	def should_be_add_to_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "Button is not presented"

	def add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		button.click()
		self.solve_quiz_and_get_code()

	def should_be_product_name(self):
		self.name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
		self.get_product_name()

	def should_be_basket_and_product_cost(self):
		self.cost = self.browser.find_element(*ProductPageLocators.BASKET_AND_PRODUCT_PRICE).text
		self.get_basket_and_product_cost()

	def should_be_name_equal_title(self):
		self.title = self.browser.find_element(*ProductPageLocators.TITLE).text
		self.get_title()

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def should_not_be_success_message_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	def add_to_basket_without_alert(self):
		button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		button.click()



