import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

Select_menu_xpath='//*[@id="sidebar"]/aside[2]/ul/li[10]/a'
speed_xpath = '//*[@id="speed-button"]/span[2]'
select_speed_xpath='//*[@id="ui-id-2"]'

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,Select_menu_xpath).click()
time.sleep(3)
print(driver.title)
driver.switch_to.frame(0)
driver.find_element(By.XPATH, speed_xpath).click()
driver.find_element(By.XPATH,select_speed_xpath).click()
time.sleep(3)