from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------- Helper Functions ----------

def wait_for_visible(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_clickable(driver, locator, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def verify_visible_and_enabled(driver, locator, name):
    element = wait_for_visible(driver, locator)
    assert element.is_displayed()
    assert element.is_enabled()
    print(f"{name} is visible and enabled")
    return element


# ---------- Test Execution ----------

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

try:
    # ---------- Login ----------
    wait_for_visible(driver, (By.NAME, "username")).send_keys("Admin")
    wait_for_visible(driver, (By.NAME, "password")).send_keys("admin123")
    wait_for_clickable(driver, (By.XPATH, "//button[@type='submit']")).click()

    # ---------- Element Availability & State Checks ----------

    # Dashboard loaded check
    wait_for_visible(driver, (By.XPATH, "//h6[text()='Dashboard']"))
    print("Dashboard loaded successfully")

    # User profile icon
    user_profile = verify_visible_and_enabled(
        driver,
        (By.CLASS_NAME, "oxd-userdropdown-tab"),
        "User Profile"
    )

    # Icon click
    user_profile.click()

    # Logout link
    logout_link = verify_visible_and_enabled(
        driver,
        (By.XPATH, "//a[text()='Logout']"),
        "Logout link"
    )

    print("Element Availability & State Checks completed")

finally:
    driver.quit()
