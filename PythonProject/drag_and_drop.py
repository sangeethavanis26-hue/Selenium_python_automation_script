import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

left_xpath = "//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']"
right_xpath ="//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']"

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.snapdeal.com/search?clickSrc=top_searches&keyword=kitchen%20product&categoryId=0&vertical=p&noOfResults=20&SRPID=topsearch")
driver.implicitly_wait(3)
left = driver.find_element(By.XPATH,left_xpath)
action = ActionChains(driver)
action.drag_and_drop_by_offset(left,50,0).perform()
time.sleep(3)
action.click_and_hold(left).pause(5).move_by_offset(60,0).release().perform()
time.sleep(5)
right = driver.find_element(By.XPATH,right_xpath)
action.click_and_hold(right).pause(5).move_by_offset(-30,0).release().perform()
time.sleep(5)