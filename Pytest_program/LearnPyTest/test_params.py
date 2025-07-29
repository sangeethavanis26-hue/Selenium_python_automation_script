import pytest


# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)
#     print("enter the url")
# #
# def testLogin(demo_fixture):
#     print("Login Successful")

# @pytest.mark.parametrize("a, b, final",  [(2,6,8),(5,8,19),(5,10,15)])
# def testAdd(a, b, final):
#     assert a+b == final


import pytest

@pytest.fixture(scope="session", autouse=True)
def OpenBroswer(browser):
    if browser == "chrome":
        print("Launch the chrome")
    elif browser == "ff":
        print("Launch the ff")
    else:
        print("provide valid browser")
    print("Login")
    print("search the product")
    yield
    print("logout the application")
    print("close browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")