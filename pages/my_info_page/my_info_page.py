from base.base_page import BasePage
from data.links import Links
from pages.my_info_page.components.personal_details import PersonalDetails
from pages.my_info_page.components.dependents import Dependents
from selenium.webdriver.support import expected_conditions as EC
import allure


class MyInfoPage(BasePage):
    _PAGE_URL = Links.MY_INFO_PAGE

    _PERSONAL_DETAILS_LINK = "//a[text()='Personal Details']"

    def __init__(self, driver):
        super().__init__(driver)
        self.personal_details_page = PersonalDetails(driver)
        self.dependents_page = Dependents(driver)

    @allure.step("Open Personal Details")
    def open_personal_details(self):
        self.wait.until(EC.element_to_be_clickable(self._PERSONAL_DETAILS_LINK)).click()


