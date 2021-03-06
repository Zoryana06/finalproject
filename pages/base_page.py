from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math

class BasePage():
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

#-------------------------------should be purchased product------------------------------------------

	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True

	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")

	def should_be_product_name(self):
		self.name = name

	def get_product_name(self):
		try:
			print(f"\nProduct name is '{self.name}'")
		except NoSuchElementException:
			print("\nName is absent")

	def should_be_basket_and_product_cost(self):
		self.cost = cost

	def get_basket_and_product_cost(self):
		try:
			print(f"Product cost is '{self.cost}'")
		except NoSuchElementException:
			print("Cost is absent")

	def should_be_name_equal_title(self):
		self.title = title

	def get_title(self):
		try:
			print(f"Product name '{self.name}' is equal title '{self.title}'\n")
		except NoSuchElementException:
			print("Product name is not equal title\n")

#------------------------------------negative checks---------------------------------------------------------

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True

#--------------------------------login link and page-----------------------------------------------------------

	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()

#-------------------------------basket button and basket page-------------------------------------------------

	def should_be_view_basket_button(self):
		assert self.is_element_present(*BasePageLocators.VIEW_BASKET), "View basket button is not presented"

	def go_to_basket(self):
		view_basket = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
		view_basket.click()

#---------------------------------register user----------------------------------------------------------------

	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"