import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



date_xpath = '//*[@id="sidebar"]/aside[2]/ul/li[6]/a'
date_input_xpath = '//*[@id="datepicker"]'
current_month_xpath = '//*[@id="ui-datepicker-div"]/div/div/span[1]'
current_year_xpath = '//*[@id="ui-datepicker-div"]/div/div/span[2]'
next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]/span'
day_xpath = '//table/tbody/tr/td/a'

driver=webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
# time.sleep(3)
driver.implicitly_wait(3)
driver.find_element(By.XPATH, date_xpath).click()
driver.switch_to.frame(0)
driver.find_element(By.XPATH,date_input_xpath).click()
time.sleep(5)

# ct = datetime.datetime.now()
# expected_date = ct.day
# expected_month = ct.month
# expected_year = ct.year
# print(expected_date)
# print(expected_year)
# print(expected_month)

expected_date = '23'
expected_month = 'November'
expected_year = '2025'

while True:
    month = driver.find_element(By.XPATH, current_month_xpath).text
    year = driver.find_element(By.XPATH, current_year_xpath).text
    if month == expected_month and year == expected_year:
        break
    else:
        driver.find_element(By.XPATH,next_button_xpath).click()
all_days = driver.find_elements(By.XPATH, day_xpath)
for a in all_days:
    if a.text == expected_date:
        a.click()
time.sleep(6)