from selenium import webdriver
from selenium.webdriver.common.by import By

# Xpath
user_name_xpath = '//*[@id="user-name"]'
password_xpath = '//*[@id="password"]'
login_xpath = '//*[@id="login-button"]'
product_xpath ='//*[@id="item_4_title_link"]'
add_to_card ='//*[@id="add-to-cart"]'
back_to_product ='//*[@id="back-to-products"]'
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.XPATH, user_name_xpath).send_keys("standard_user")
driver.find_element(By.XPATH, password_xpath).send_keys("secret_sauce")
driver.find_element(By.XPATH, login_xpath).click()
driver.find_element(By.XPATH,product_xpath).click()
driver.find_element(By.XPATH,add_to_card).click()
driver.find_element(By.XPATH,back_to_product).click()

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(all_links)

for link in all_links:
    url = link.get_attribute('href')
    print(url)

driver.find_element(By.LINK_TEXT, 'Sauce Labs Backpack').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart').click()
print(driver.title)
# driver.quit()
