from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()  # переход на страницу с login
    login_page = LoginPage(browser, browser.current_url)  #  создание экз. клааса страницы login
    login_page.should_be_login_page()  # запуск методов проверок url и наличия форм

