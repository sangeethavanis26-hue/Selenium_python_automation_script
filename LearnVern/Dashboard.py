import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# 2. Dashboard Page Validation

# positive scenario
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH, '//button[normalize-space()="Login"]').click()

# Dashboard page load verification
dashboard_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[normalize-space()='Dashboard']")))
print("Dashboard page validated")

# Page title
assert "OrangeHRM in driver.title"
print("Page title verified")

# URL validation
assert "dashboard" in driver.current_url
print("URL validated")

# Header
header = driver.find_element(By.XPATH, "//div[@class='oxd-topbar-header']")
assert header.is_displayed()
print("Header validated")

# sidebar
sidebar = driver.find_element(By.XPATH, "//div[@class='oxd-sidepanel-body']")
assert sidebar.is_displayed()
print("sidebar validated")

# user profile visibility
user_profile = driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
assert user_profile.is_displayed()
print("user profile visibility validated")


# 4. Element Availability & State Checks


# Verify elements are visible and enabled
# Handle dynamic loading using explicit waits
# user profile enabled
user_profile = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='oxd-userdropdown-tab']")))
assert user_profile.is_enabled()
print("user profile visible and enabled")

# Handle dynamic loading using explicit waits
# Validate buttons, links, and icons availability
user_profile.click()
log_out= wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Logout']")))
assert log_out.is_displayed()
assert log_out.is_enabled()
print("Logout link is available and clickable")
# log_out.click()

# 5. Table & Listing Validation
# Verify table headers

pim_menu = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
driver.execute_script("arguments[0].scrollIntoView(true);",pim_menu)
pim_menu.click()

time.sleep(5)
headers =  driver.find_elements(By.XPATH, "//div[@role='columnheader']//span")
for h in headers:
    print(h.get_attribute("innerText"))

rows = driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
print(len(rows))
assert len(rows) > 0


# Search, filter
driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys('Abhay Kumar Kaushik')
driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
time.sleep(3)

filter_row = driver.find_elements(By.XPATH, "//div[contains(@class,'oxd-table-row')]")
print(len(filter_row))

# pagination handling

next_button = driver.find_elements(By.XPATH,"//button[contains(@class,'oxd-pagination-page-item')]")
# driver.execute_script("arguments[0].scrollIntoView(true);",next_button)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
if next_button:
    next_button[0].click()
    print("next page clicked")

else:
    print(("pagination is not available"))