from xml.dom.xmlbuilder import Options

import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    chrome_option =Options()
    # chrome_option.add_experiental_option("detach", True)
    service = Service(ChromeDriverManager().install())