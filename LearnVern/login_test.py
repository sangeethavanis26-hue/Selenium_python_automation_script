import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Login Automation

# positive scenario
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()
assert 'orangehrmlive' in driver.current_url
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
driver.quit()

# Negative scenario
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("afg")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("asdf")
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()
driver.implicitly_wait(10)
inv = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
assert 'Invalid credentials' in inv
driver.quit()

# Required scenario
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("")
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()
driver.implicitly_wait(10)
req = driver.find_element(By.XPATH, "//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]").text
assert 'Required' in req
driver.quit()