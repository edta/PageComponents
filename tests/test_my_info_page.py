import time
import pytest
import allure

from base.base_test import BaseTest
@allure.feature("My Info feature")
class TestMyInfoPage(BaseTest):
    @allure.title("My info")
    @pytest.mark.parametrize("add_users", [2], indirect=True)
    def test_my_info(self, add_users):
        user2, user3 = add_users
        self.login_page().open()
        self.login_page().is_opened()
        self.login_page().login_as(self.credentials.LOGIN, self.credentials.PASSWORD)
        time.sleep(3)
        self.login_page(user2).open()
        time.sleep(3)
        self.login_page(user3).open()
        self.dashboard_page.is_opened()
        self.dashboard_page.go_to_menu_link(self.menu.my_info)
        self.my_info_page.is_opened()
        self.my_info_page.open_personal_details()
        self.my_info_page.personal_details_page.enter_name()
        self.dashboard_page.go_to_menu_link(self.menu.performance)