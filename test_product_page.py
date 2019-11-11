from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest

simple_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	page = ProductPage(browser, promo_link)
	page.open()
	page.should_be_purchased_product()

#-------------------------------------------negative checks ----------------------------------------------

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.add_to_basket_without_alert()
	page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.add_to_basket_without_alert()
	page.should_not_be_success_message_disappeared()

#----------------------------------guest should see and go to login page------------------------

def test_guest_should_see_login_link_on_product_page(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.go_to_login_page()

#----------------------------------inheritance and negative check--------------------------

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	page = ProductPage(browser, simple_link)
	page.open()
	page.go_to_basket()
	page = BasketPage(browser, browser.current_url)
	page.should_be_empty_basket()

#-----------------------------------register user-------------------------------------------

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		self.page = ProductPage(browser, simple_link)
		self.page.open()
		self.page.go_to_login_page()
		self.page = LoginPage(browser, browser.current_url)
		self.page.register_new_user()
		self.page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, simple_link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		page = ProductPage(browser, promo_link)
		page.open()
		page.should_be_purchased_product()