import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import Config
from utils.driver_factory import DriverFactory

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.get(Config.BASE_URL)
    login = LoginPage(driver)
    login.enter_username(Config.VALID_USERNAME)
    login.enter_password(Config.VALID_PASSWORD)
    login.click_login()
    assert "dashboard" in driver.current_url.lower()

def test_invalid_login(driver):
    driver.get(Config.BASE_URL)
    login = LoginPage(driver)
    login.enter_username("wronguser")
    login.enter_password("wrongpass")
    login.click_login()
    assert "Invalid credentials" in login.get_invalid_credential()

def test_error_message(driver):
    driver.get(Config.BASE_URL)
    login = LoginPage(driver)
    login.enter_username("")
    login.enter_password("")
    login.click_login()
    assert "Required" in login.get_error_message()