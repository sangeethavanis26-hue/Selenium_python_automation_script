import time

from selenium import webdriver
from selenium.webdriver.common.by import By
text_xpath = '//*[@id="standard-collection-wdgt"]/div/h2'

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(3)
ele = driver.find_element(By.XPATH,text_xpath)
driver.execute_script("arguments[0].scrollIntoView()", ele)
time.sleep(3)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500)")
time.sleep(3)
driver.refresh()
time.sleep(3)
