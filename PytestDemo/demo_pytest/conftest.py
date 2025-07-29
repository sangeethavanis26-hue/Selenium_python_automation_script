import pytest


# @pytest.fixture(scope= "package", autouse=True)
@pytest.fixture(scope= "session", autouse=True)
def setUp():
    print("Lunch Browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close browser")