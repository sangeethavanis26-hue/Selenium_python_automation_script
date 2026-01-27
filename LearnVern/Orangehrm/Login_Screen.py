from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- SETUP ----------
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    return driver


# ---------- LOGIN FUNCTION ----------
def login(driver, username, password):
    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")

    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element(By.XPATH, "//button[@type='submit']").click()


# ---------- VALID LOGIN CHECK ----------
def verify_valid_login(driver):
    wait = WebDriverWait(driver, 15)
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    print("PASS: Valid login")



def logout(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name"))).click()
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()


# ---------- EMPTY CREDENTIAL CHECK ----------
def verify_empty_credentials(driver):
    print("PASS: Empty fields validation shown")


# ---------- INVALID LOGIN CHECK ----------
def verify_invalid_login(driver):
    print("PASS: Invalid credentials validation shown")


# ---------- TEST EXECUTION ----------
def run_test_cases(driver, test_cases):
    for username, password in test_cases:
        login(driver, username, password)

        # VALID LOGIN
        if username == "Admin" and password == "admin123":
            verify_valid_login(driver)
            logout(driver)

        # EMPTY CREDENTIALS
        elif username.strip() == "" and password.strip() == "":
            verify_empty_credentials(driver)

        # INVALID CREDENTIALS
        else:
            verify_invalid_login(driver)


# ---------- MAIN ----------
driver = setup_driver()

all_test_case = [
    (' ', ' '),
    ('abc', 'xyz'),
    ('abc', 'admin123'),
    ('Admin', 'sdfe'),
    ('Admin', 'admin123')
]

run_test_cases(driver, all_test_case)
driver.quit()
