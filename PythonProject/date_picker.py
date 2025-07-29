# import time, datetime
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# date_picker_xpath = '//*[@id="sidebar"]/aside[2]/ul/li[6]/a'
# date_input_xpath ='//*[@id="datepicker"]'
# next_button_xpath = '//*[@id="ui-datepicker-div"]/div/a[2]/span'
# current_month_xpath = '//*[@id="ui-datepicker-div"]/div/div/span[1]'
# current_year_xpath ='//*[@id="ui-datepicker-div"]/div/div/span[2]'
# date_xpath = '//table/tbody/tr/td/a'
#
# driver=webdriver.Chrome()
# driver.get("https://jqueryui.com/")
# driver.maximize_window()
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, date_picker_xpath).click()
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, date_input_xpath).click()
# time.sleep(3)
#
# expected_date = "25"
# expected_month = "November"
# expected_year = "2025"
#
# # ct = datetime.datetime.now()
# # print(ct.day)
# # print(ct.month)
# # print(ct.year)
#
# while True:
#     current_month = driver.find_element(By.XPATH, current_month_xpath).text
#     current_year = driver.find_element(By.XPATH, current_year_xpath).text
#
#     if current_month == expected_month and current_year == expected_year:
#         break
#     else:
#         driver.find_element(By.XPATH,next_button_xpath).click()
#
# all_dates = driver.find_elements(By.XPATH, date_xpath)
# for date in all_dates:
#     if date.text == expected_date:
#         date.click()
# time.sleep(3)