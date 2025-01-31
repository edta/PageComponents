import time

import allure

from base.base_test import BaseTest
@allure.feature("My Info feature")
class TestMyInfoPage(BaseTest):
    @allure.title("My info")
    def test_my_info(self):
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(self.credentials.LOGIN, self.credentials.PASSWORD)

        admin = self.browser_factory()
        self.login_page(admin).open()
        self.login_page(admin).login_as(self.credentials.LOGIN, self.credentials.PASSWORD)

        admin2= self.browser_factory()
        self.login_page(admin2).open()
        self.login_page(admin2).login_as(self.credentials.LOGIN, self.credentials.PASSWORD)

        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_menu_link(self.menu.my_info)
        self.my_info_page.is_opened()
        self.my_info_page.open_personal_details()
        self.my_info_page.personal_details_page.enter_name()
        self.dashboard_page.go_to_menu_link(self.menu.performance)