import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Windows.html")
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(3)
print(driver.title)
time.sleep(3)
# driver.find_element(By.XPATH,'//*[@id="PopUp"]').click()
# driver.find_element(By.XPATH,"//*[@id='Seperate']/button").click()
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="singleFileInput"]').click()
driver.find_element(By.XPATH,'//*[@id="singleFileInput"]').send_keys("C:\\Users\\nithi\\OneDrive\\Documents\\mic.pdf")

time.sleep(10)
# driver.find_element(By.XPATH, )
# Parent = driver.current_window_handle
# print(Parent.title())
# all_win = driver.window_handles
# for a in all_win:
#     driver.switch_to.window(a)
#     print(driver.title)