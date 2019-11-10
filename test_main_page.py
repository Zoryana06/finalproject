from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()

def test_guest_can_go_to_login_page(browser):
	page = MainPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
	page = MainPage(browser, link)
	page.open()
	page.go_to_login_page()
	page = LoginPage(browser, browser.current_url)
	page.should_be_login_page()