import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Make_appointment_Xpath='//*[@id="btn-make-appointment"]'
facility_xpath= "//*[@id='combo_facility']"
Read_mission_Class="checkbox-inline"
Health_care_program_Xpath='//*[@id="radio_program_medicaid"]'
comment_Xpath='//*[@id="txt_comment"]'
Book_appointment_tag_name="button"

driver = webdriver.Chrome()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,Make_appointment_Xpath).click()
time.sleep(15)

dropdown=Select(driver.find_element(By.XPATH,facility_xpath))
dropdown.select_by_index(2)
# driver.implicitly_wait(10)
# time.sleep(10)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH,facility_xpath)))

radio_button = driver.find_element(By.CLASS_NAME,Read_mission_Class)

if radio_button.is_selected():
    print("Already Enabled")
else:
    radio_button.click()
    print("Now Enabled")




driver.find_element(By.XPATH,Health_care_program_Xpath).click()
driver.find_element(By.XPATH,comment_Xpath).send_keys("Thanks for visiting for site")
# driver.find_element(By.TAG_NAME,Book_appointment_tag_name).click()
time.sleep(3)