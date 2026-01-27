from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com")
    return driver


def login(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    print("Login successful")


def open_pim_page(driver):
    wait = WebDriverWait(driver, 20)
    pim_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']/ancestor::a")))
    pim_menu.click()

    # wait directly for table (stable)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-table")))
    print("PIM page opened")


def scroll_to_table(driver):
    table = driver.find_element(By.CLASS_NAME, "oxd-table")
    driver.execute_script("arguments[0].scrollIntoView(true);", table)


def print_table_headers(driver):
    print("Table headers")

    wait = WebDriverWait(driver, 10)

    headers = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//div[contains(@class,'oxd-table-header-cell')]")
        )
    )

    print("Header count:", len(headers))

    for header in headers:
        print(header.text)



def print_row_count(driver):
    wait = WebDriverWait(driver, 20)
    rows = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    ))
    print("Row count:", len(rows))


def search_employee(driver):
    wait = WebDriverWait(driver, 20)

    search_box = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//label[text()='Employee Name']/ancestor::div//input")
    ))
    search_box.clear()
    search_box.send_keys("Abhay Kumar Kaushik")

    search_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[normalize-space()='Search']")
    ))

    # scroll button into view
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", search_btn)

    search_btn.click()

    rows = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
    ))

    print("Rows after search:", len(rows))

# ---------------- MAIN EXECUTION ----------------

driver = open_browser()

login(driver)
open_pim_page(driver)
scroll_to_table(driver)
print_table_headers(driver)
print_row_count(driver)
search_employee(driver)

driver.quit()