import time

from selenium import webdriver
from selenium.webdriver.common.by import By
element_xpath = "//h2[normalize-space()='Sponsored companies']"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.naukri.com/")
driver.implicitly_wait(3)
driver.execute_script("window.scrollBy(0,100)")
time.sleep(3)
element = driver.find_element(By.XPATH, element_xpath)
driver.execute_script("arguments[0].scrollIntoView()",element)
time.sleep(5)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-100)")
time.sleep(3)