import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="moneyiframe"]'))
driver.find_element(By.XPATH, '//*[@id="bseindex"]').click()
driver.switch_to.default_content()
time.sleep(3)