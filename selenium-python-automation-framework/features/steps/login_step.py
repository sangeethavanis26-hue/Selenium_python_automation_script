from behave import given, when, then
from pages.login_page import LoginPage
from utils.driver_factory import DriverFactory
from utils.config import Config
from selenium.webdriver.common.by import By
import time

@given("I open the OrangeHRM login page")
def step_open_login_page(context):
    context.driver = DriverFactory.get_driver()
    context.driver.get(Config.BASE_URL)
    context.login_page = LoginPage(context.driver)

@when("I enter valid username and password")
def step_valid_credentials(context):
    context.login_page.enter_username(Config.VALID_USERNAME)
    context.login_page.enter_password(Config.VALID_PASSWORD)

@when("I enter invalid username or password")
def step_invalid_credentials(context):
    context.login_page.enter_username("invalid")
    context.login_page.enter_password("invalid123")

@when("I leave username and password empty")
def step_empty_credentials(context):
    context.login_page.enter_username("")
    context.login_page.enter_password("")

@when("I click the login button")
def step_click_login(context):
    context.login_page.click_login()
    time.sleep(2)

@then("I should see the dashboard page")
def step_verify_dashboard(context):
    assert "dashboard" in context.driver.current_url.lower()
    context.driver.quit()

@then("I should see an error message")
def step_verify_error_message(context):
    error = context.login_page.get_invalid_credential()
    assert "Invalid credentials" in error
    context.driver.quit()

@then("I should see a validation message")
def step_verify_validation_message(context):
    error = context.login_page.get_error_message()
    time.sleep(5)
    assert "Required" in error
    context.driver.quit()
