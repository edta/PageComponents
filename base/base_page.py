import time

from faker import Faker
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from metaclasses.meta_locator import MetaLocator
import allure

class Navigation(metaclass=MetaLocator):
    my_info = "//span[text()='My Info']"
    performance = "//span[text()='Performance']"

class BasePage(metaclass=MetaLocator):

    # _MY_INFO_LINK = "//span[text()='My Info']"
    # _PERFORMANCE_LINK = "//span[text()='Performance']"

    def __init__(self, driver):
        self.menu = Navigation()
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, 1)
        self.fake = Faker()

    @allure.step("Open page")
    def open(self):
        with allure.step(f"Open page {self._PAGE_URL}"):
            self.driver.get(self._PAGE_URL)
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    def is_opened(self):
        with allure.step(f"Page {self._PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self._PAGE_URL))

    # @allure.step("Open My Info page")
    # def go_to_my_info(self):
    #     self.wait.until(EC.element_to_be_clickable(self._MY_INFO_LINK)).click()

    @allure.step("Open menu link")
    def go_to_menu_link(self, menu_link):
        with allure.step(f"Open menu link"):
            self.wait.until(EC.element_to_be_clickable(menu_link)).click()
