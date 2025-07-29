import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email_id = "Form_submitForm_EmailHomePage"
trail_name = "action_request"
username_xpath = "//*[@id='Form_getForm_subdomain']"
fullname_selector = "#Form_getForm_Name"
priceName_class = "text"
email_class = "field email text"
country_xpath = "//select[@id='Form_getForm_Country']"
NoOfEmployee_xpath = '//*[@id="Form_getForm_NoOfEmployees"]'

driver = webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
driver.find_element(By.ID, email_id).send_keys("sangeemani2000@gmail.com")
wait = WebDriverWait(driver, 30)
element = wait.until(EC.visibility_of_element_located((By.ID, email_id)))
name = driver.find_element(By.NAME, trail_name)
# name.click()
if name.is_selected():
    print("not selected")
else:
    name.click()
    print("selected")
print (driver.title)
driver.find_element(By.XPATH, username_xpath).send_keys("Sangeetha")
driver.find_element(By.CSS_SELECTOR, fullname_selector).send_keys("Sangeethavani")
all_links = driver.find_element(By.PARTIAL_LINK_TEXT, 'Pric')
all_links.click()
dropdown = Select(driver.find_element(By.XPATH, country_xpath))
dropdown.select_by_index(5)
driver.find_element(By.XPATH, country_xpath).click()
options = driver.find_elements(By.TAG_NAME, "option")
# options.click()
for option in options:
    if option.text == '51 - 200':
        option.click()
        print("select this option",option)
        break


# driver.find_element(By.TAG_NAME, 'input').send_keys("Arjun")
# driver.find_element(By.CLASS_NAME,email_class).send_keys("arjun@1234")
# Find all <a> elements
# all_links = driver.find_elements(By.TAG_NAME, "a")
# print("All link texts found on the page:")
# for link in all_links:
#     url = link.get_attribute('href')
#     print(url)
#     print(link.text)
driver.implicitly_wait(10)
# time.sleep(10)
driver.close()

