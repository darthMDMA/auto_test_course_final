from .pages.main_page import MainPage

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"