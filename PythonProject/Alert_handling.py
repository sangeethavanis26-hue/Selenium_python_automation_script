import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

Alert_xpath="//*[@id='alertexamples']"
Confirm_xpath="//*[@id='confirmexample']"
Prompt_xpath="//*[@id='promptexample']"

driver=webdriver.Chrome()
driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,Alert_xpath).click()
Alert(driver).accept()
time.sleep(3)
# driver.switch_to.alert.accept()
# time.sleep(3)
driver.find_element(By.XPATH,Confirm_xpath).click()
Alert(driver).dismiss()
time.sleep(3)
# message = driver.switch_to.alert.text
# print(message)
# driver.switch_to.alert.dismiss()
# time.sleep(3)
driver.find_element(By.XPATH,Prompt_xpath).click()
time.sleep(2)
Alert(driver).send_keys("Thank you so much")
Alert(driver).accept()
time.sleep(7)
# driver.switch_to.alert.send_keys("Thank you so much")
# driver.switch_to.alert.accept()
# time.sleep(3)