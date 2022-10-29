from time import sleep

from src.pages import LoginPage


class TestLogin:
    def test_1(self, driver, browsers):
        LoginPage(driver[browsers]).open_page()
        LoginPage(driver[browsers]).get_page_posts()
        sleep(3)

    def test_2(self, driver, browsers):
        LoginPage(driver[browsers]).open_page()
        sleep(3)


