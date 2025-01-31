from selenium import webdriver
import pytest

def get_driver():
    driver = webdriver.Chrome()
    return driver
@pytest.fixture(autouse=True)
def driver(request):
    driver = get_driver()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def add_users(request):
    user_count = request.param
    drivers = []
    for _ in range(user_count):
        driver = get_driver()
        drivers.append(driver)
    yield drivers
    for driver in drivers:
        driver.quit()