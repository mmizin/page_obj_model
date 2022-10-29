from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from src.locators import LoginPageLocators


class BasePage():
    wait_time = 8

    def __init__(self, driver):
        self.driver = driver

    @property
    def wait(self):
        return WebDriverWait(self.driver, self.wait_time)

    @staticmethod
    def get_elements():
        try:
            pass
        except Exception as e:
            print(f'We couldn\'t  get elements')



class LoginPage(BasePage):
    url = 'https://blog.ethereum.org/'

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url=url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(LoginPageLocators.page_1))

    def get_page_posts(self):
        page_posts = self.driver.find_elements(*LoginPageLocators.page_posts)
        print(page_posts)









