import time

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.invalid_credential = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
        self.required_message = (By.XPATH, "//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_invalid_credential(self):
        return self.driver.find_element(*self.invalid_credential).text

    def get_error_message(self):
        time.sleep(5)
        return self.driver.find_element(*self.required_message).text

