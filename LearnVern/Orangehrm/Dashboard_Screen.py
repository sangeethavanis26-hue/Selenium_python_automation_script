from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRMDashboard:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visibility(self, locator):
        """Wait until element is visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def login(self, username, password):
        self.wait_for_visibility((By.XPATH, "//input[@placeholder='Username']")).send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()

    def validate_dashboard_loaded(self):
        dashboard_header = self.wait_for_visibility(
            (By.XPATH, "//h6[normalize-space()='Dashboard']")
        )
        assert dashboard_header.is_displayed()
        print("Dashboard page validated")

    def validate_page_title(self):
        assert "OrangeHRM" in self.driver.title
        print("Page title verified")

    def validate_url(self):
        self.wait.until(EC.url_contains("dashboard"))
        assert "dashboard" in self.driver.current_url
        print("URL validated")

    def validate_header(self):
        header = self.wait_for_visibility((By.XPATH, "//div[@class='oxd-topbar-header']"))
        assert header.is_displayed()
        print("Header validated")

    def validate_sidebar(self):
        sidebar = self.wait_for_visibility((By.XPATH, "//div[@class='oxd-sidepanel-body']"))
        assert sidebar.is_displayed()
        print("Sidebar validated")

    def validate_user_profile(self):
        user_profile = self.wait_for_visibility(
            (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        )
        assert user_profile.is_displayed()
        print("User profile visibility validated")


# ---------- Test Execution ----------

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")

dashboard = OrangeHRMDashboard(driver)

# Positive login scenario
dashboard.login("Admin", "admin123")

# Dashboard validations
dashboard.validate_dashboard_loaded()
dashboard.validate_page_title()
dashboard.validate_url()
dashboard.validate_header()
dashboard.validate_sidebar()
dashboard.validate_user_profile()

driver.quit()