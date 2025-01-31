from base.base_page import BasePage
from data.links import Links
import allure
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    _PAGE_URL = Links.LOGIN_PAGE
    _USERNAME_FIELD = "//input[@name='username']"
    _PASSWORD_FIELD = "//input[@name='password']"
    _LOGIN_BUTTON = "//button[@type='submit']"

    @allure.step("Login into account")
    def login_as(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON))
        self.driver.find_element(*self._USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()
