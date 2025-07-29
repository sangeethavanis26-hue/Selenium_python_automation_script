import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# def test_open_google():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.google.com")
#     assert "Google" in driver.title
#     # driver.quit()
#
# def test_max_window():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.get("https://www.google.com")
#     driver.maximize_window()


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()
    yield driver  # Return the driver to the test
    driver.quit()  # Quit after test is done

def test_open_google(driver):
    # driver.get("https://www.google.com")

    assert "Google" in driver.title

def test_max_window(driver):

    # driver.maximize_window()
    print(driver.current_url)
    assert driver.title != ""
