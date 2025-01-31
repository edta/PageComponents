from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class PersonalDetails(BasePage):
    _FIRST_NAME_FIELD = "//input[@name='firstName']"
    _MIDDLE_NAME_FIELD = "//input[@name='middleName']"
    _LAST_NAME_FIELD = "//input[@name='lastName']"

    @allure.step("Enter name")
    def enter_name(self):
        (self.wait.until(
            EC.element_to_be_clickable(self._FIRST_NAME_FIELD)).
         send_keys(self.fake.first_name()))
        (self.wait.until(
            EC.element_to_be_clickable(self._MIDDLE_NAME_FIELD)).
         send_keys(self.fake.first_name()))
        (self.wait.until(
            EC.element_to_be_clickable(self._LAST_NAME_FIELD)).
         send_keys(self.fake.last_name()))

