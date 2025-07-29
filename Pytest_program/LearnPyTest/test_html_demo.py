import time


def test_google_search(browser):
    # Visit a URL
    browser.get("https://www.redbus.com/")
    # Force fail to test screenshot
    assert "RedBus" in browser.title
    time.sleep(5)


def testAddToCard(browser):
    assert 5 == 5  # This will also fail and take screenshot
