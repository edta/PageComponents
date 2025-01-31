import os
from selenium import webdriver
from pages.my_info_page.my_info_page import MyInfoPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from data.credentials import Credentials
from base_page import Navigation


class BaseTest:

    def setup_method(self):
        self.menu = Navigation()
        self.credentials = Credentials()
        self.my_info_page = MyInfoPage(self.driver)
        self.login_page = lambda driver=self.driver: LoginPage(driver)
        self.dashboard_page = DashboardPage(self.driver)


