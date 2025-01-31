import os
from selenium import webdriver
from pages.my_info_page.my_info_page import MyInfoPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.credentials import Credentials
from base_page import Navigation


class BaseTest:

    def setup_method(self):
        self.default_user = self.browser_factory()
        self.menu = Navigation()
        self.credentials = Credentials()
        self.my_info_page = MyInfoPage(self.default_user)
        self.login_page = lambda driver=self.default_user: LoginPage(driver)
        self.dashboard_page = DashboardPage(self.default_user)

    def browser_factory(self):
        browser = os.environ['BROWSER']
        if browser == 'chrome':
            driver = webdriver.Chrome()
        elif browser == 'firefox':
            driver = webdriver.Firefox()
        return driver

    def teardown_method(self):
        self.default_user.quit()
