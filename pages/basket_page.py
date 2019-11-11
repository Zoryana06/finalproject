from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"

#----------------negative check for 'test_guest_cant_see_product_in_basket_opened_from_main_page' and----------
#-----------------------------------'test_guest_cant_see_product_in_basket_opened_from_main_page' tests

	def should_not_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is empty, but should not be"