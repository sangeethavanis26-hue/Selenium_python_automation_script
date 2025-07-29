import time
from datetime import datetime
# from html.parser import commentclose
from tkinter import Radiobutton
from turtledemo.clock import current_day

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

title_xpath = "//h1[normalize-space()='CURA Healthcare Service']"
make_appointment_button_xpath = "//a[@id='btn-make-appointment']"
username_xpath = "//input[@id='txt-username']"
password_xpath = "//input[@id='txt-password']"
login_button_xpath = "//button[@id='btn-login']"
make_appointment_xpath = "//*[@id='appointment']/div/div/div/h2"
facility_xpath = "//*[@id='combo_facility']"
apply_readmission_checkbox_xpath = "//*[@id='chk_hospotal_readmission']"
medicaid_radiobutton_xpath = "//input[@id='radio_program_medicaid']"
# calender_xpath = "//span[@class='glyphicon glyphicon-calendar']"
comment_xpath = "//textarea[@id='txt_comment']"
book_appointment_xpath = "//button[@id='btn-book-appointment']"
date_xpath = "//span[@class='glyphicon glyphicon-calendar']"
day_xpath ="//td[@class='day'][normalize-space()='25']"
appointment_conformation_xpath = "//h2[normalize-space()='Appointment Confirmation']"
go_to_homepage_xpath = "//a[normalize-space()='Go to Homepage']"



driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH, title_xpath)
driver.find_element(By.XPATH, make_appointment_button_xpath).click()
time.sleep(3)
driver.find_element(By.XPATH, username_xpath).send_keys("John Doe")
driver.find_element(By.XPATH,password_xpath).send_keys("ThisIsNotAPassword")
driver.find_element(By.XPATH, login_button_xpath).click()
driver.find_element(By.XPATH, make_appointment_xpath)
drop_down = driver.find_element(By.XPATH, facility_xpath)
drop = Select(drop_down)
drop.select_by_index(2)
driver.find_element(By.XPATH, apply_readmission_checkbox_xpath).click()
medicaid_radio_button = driver.find_element(By.XPATH, medicaid_radiobutton_xpath)
medicaid_radio_button.click()
time.sleep(4)
print(medicaid_radio_button.get_attribute('checked'))
if medicaid_radio_button.is_selected():
    print("medicaid selected")
else:
    print("Default one selected")

date = driver.find_element(By.XPATH, date_xpath)
time.sleep(3)
driver.find_element(By.XPATH,day_xpath).click()
time.sleep(3)
driver.find_element(By.XPATH, comment_xpath).send_keys("Book Appointment")
driver.find_element(By.XPATH, book_appointment_xpath).click()
time.sleep(3)
driver.find_element(By.XPATH, appointment_conformation_xpath)
driver.find_element(By.XPATH, go_to_homepage_xpath).click()
time.sleep(4)
driver.quit()
