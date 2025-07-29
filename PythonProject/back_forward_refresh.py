import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.redbus.in/")
# driver.save_screenshot("C:\\Selenium_Project\\Screenshot\\redbus1.png")
# time.sleep(3)
driver.get_screenshot_as_file("C:\\Selenium_Project\\Screenshot\\image.png")
time.sleep(3)




# time.sleep(3)
# driver.get("https://www.google.com/")
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)