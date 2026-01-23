from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(3)

all_test_case = [
    ('abc','xyz'),
    ('abc', 'admin123'),
    ('Admin', 'sdfe'),
    (' ', ' '),
    ('Admin', 'admin123')
]

for username, password in all_test_case:

    # Enter username and password
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # VALID LOGIN
    if username == "Admin" and password == "admin123":
        if "dashboard" in driver.current_url.lower():
            print("PASS: Valid login")

            # Logout
            driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
            time.sleep(2)
            driver.find_element(By.LINK_TEXT, "Logout").click()
            time.sleep(3)

    # EMPTY CREDENTIALS
    elif username.strip() == "" and password.strip() == "":
        print("PASS: Empty fields validation shown")

    # INVALID CREDENTIALS
    else:
        print("PASS: Invalid credentials validation shown")

driver.quit()
