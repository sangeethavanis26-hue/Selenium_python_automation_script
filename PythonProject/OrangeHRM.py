import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

login_xpath = "//input[@placeholder='Username']"
password_xpath = "//input[@placeholder='Password']"
login_button_xpath = "//button[normalize-space()='Login']"
dashboard_xpath = "//a[@class='oxd-main-menu-item active']"
recruitment_xpath = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment']"
vacancy_xpath = "//div[@role='columnheader'][normalize-space()='']"
record_checkbox = "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]"
delete_selected_xpath = "//button[normalize-space()='Delete Selected']"
no_cancel_xpath = "//button[normalize-space()='No, Cancel']"
table_heading_xpath = "//div[@class='oxd-table-header']//div[@role='row']"
table_context_xpath = "//div[@class='oxd-table-body']"
candidate_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5"
vacancy_title_dropdown = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i"
candidate_name_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/div/div[1]/div/div[2]/div/div/input"
search_button = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[4]/button[2]"
shortlist_dropdown_xpath = "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i"
records_found_xpath= "//span[normalize-space()='(19) Records Found']"



driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.maximize_window()
driver.find_element(By.XPATH, login_xpath).send_keys("Admin")
driver.find_element(By.XPATH,password_xpath).send_keys("admin123")
driver.find_element(By.XPATH,login_button_xpath).click()
time.sleep(3)
print(driver.title)
driver.find_element(By.XPATH,dashboard_xpath)
driver.find_element(By.XPATH,recruitment_xpath).click()
time.sleep(3)

# # driver.find_element(By.XPATH, candidate_xpath)
# option = driver.find_element(By.XPATH,vacancy_title_dropdown).click()
# options = WebDriverWait(driver, 5).until(
#     EC.presence_of_all_elements_located((By.XPATH, ))  # Adjust XPath as needed
# )
#
# if options:
#     options[1].click()
# # driver.execute_script("arguments[0].click();", option)
# time.sleep(3)
# vacancy = Select(vacancy_dd)
# vacancy.select_by_visible_text("Senior QA Lead")
# candidate = driver.find_element(By.XPATH, candidate_name_xpath)
# candidate.send_keys("John")
# candidate.

# shortlist_dd = driver.find_element(By.XPATH, shortlist_dropdown_xpath)
# shortlist = Select(shortlist_dd)
# shortlist.select_by_visible_text("Shortlisted")
# driver.find_element(By.XPATH, search_button).click()
# driver.find_element(By.XPATH, records_found_xpath)


#
vacancy_text = driver.find_element(By.XPATH, vacancy_xpath)
actions = ActionChains(driver)
actions.move_to_element(vacancy_text).perform()
record_selected = driver.find_element(By.XPATH, record_checkbox)
record_selected.click()
driver.find_element(By.XPATH, delete_selected_xpath).click()
driver.find_element(By.XPATH, no_cancel_xpath).click()
record_selected.click()
time.sleep(3)

headers = driver.find_elements(By.XPATH, table_heading_xpath)
for header in headers:
    print(header.text)

table_content = driver.find_elements(By.XPATH, table_context_xpath)
for context in table_content:
    print(context.text)

driver.quit()