import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver | None = None
#
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.get_plugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when in ("setup", "call"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = (
                    '<div><img src="%s" alt="screenshot" style="width:304px;height:228px" '
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                )
                extras.append(pytest_html.extras.html(html))
        report.extras = extras
#
#
def _capture_screenshot(name):
    if driver:
        driver.get_screenshot_as_file(name)

def pytest_html_report_title(report):
    report.title = "Automation Report"

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        options = Options()
        options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
