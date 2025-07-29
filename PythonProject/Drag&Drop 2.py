import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

drag_xpath='//*[@id="draggable"]/p'
drop_xpath='//*[@id="droppable"]'
double_click_xpath = '//*[@id="authentication"]/button'
right_click_xpath = '//*[@id="authentication"]/span'
copy_xpath = '//*[@id="authentication"]/ul/li[3]/span'

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(4)
element = driver.find_element(By.XPATH,double_click_xpath)
element1 = driver.find_element(By.XPATH,right_click_xpath)
action=ActionChains(driver)
action.double_click(element).perform()
driver.switch_to.alert.accept()
time.sleep(4)

action.context_click(element1).perform()
driver.find_element(By.XPATH,copy_xpath).click()
driver.switch_to.alert.accept()
time.sleep(4)












# drag=driver.find_element(By.XPATH,drag_xpath)
# drop=driver.find_element(By.XPATH,drop_xpath)
# driver.implicitly_wait(4)
# action=ActionChains(driver)
# action.drag_and_drop(drag,drop).perform()
# driver.switch_to.alert.accept()
# time.sleep(3)