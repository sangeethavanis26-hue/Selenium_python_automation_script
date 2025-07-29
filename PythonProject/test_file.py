import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

email_id = "Form_submitForm_EmailHomePage"
free_name = "action_request"
full_name_xpath = "//*[@id='Form_getForm_Name']"
phone_classname = "text"
full_css = "#Form_getForm_FullName"
Country_xpath = '//*[@id="Form_getForm_Country"]'
noOfEmployee_xpath = '//*[@id="Form_getForm_NoOfEmployees"]'

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
driver.find_element(By.ID, email_id).send_keys("san123@gmail.com")
driver.find_element(By.NAME, free_name).click()
driver.find_element(By.XPATH, full_name_xpath).send_keys("Madhu")
# driver.find_element(By.CLASS_NAME,phone_classname).send_keys("674850395")
# driver.find_element(By.LINK_TEXT,"Pricing").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Pric").click()
driver.find_element(By.CSS_SELECTOR, full_css).send_keys("Sangeetha")
dropdown = Select(driver.find_element(By.XPATH, Country_xpath))
dropdown.select_by_index(5)
time.sleep(3)
dropdown.select_by_value("India")
time.sleep(3)
dropdown.select_by_visible_text("Iceland")
# time.sleep(3)

# driver.find_element(By.XPATH, noOfEmployee_xpath).click()
option = driver.find_elements(By.TAG_NAME, 'option')

for i in option:
    if i.text == '51 - 200':
        i.click()
        break
time.sleep(3)

links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    # url = link.get_attribute('href')
    # print(url)
    print(link.text)