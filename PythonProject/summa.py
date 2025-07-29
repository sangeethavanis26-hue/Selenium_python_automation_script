import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys("07/01/2025")
time.sleep(4)
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, '//*[@id="simple-tab-4"]/span[1]/text()')
# origin_date = driver.find_element(By.XPATH, '//*[@id="simple-tab-4"]/span[1]/text()')
# origin_date.click()
# wait = WebDriverWait(driver, 10)
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "MuiBox-root css-18jnpb8")))
# time.sleep(3)
