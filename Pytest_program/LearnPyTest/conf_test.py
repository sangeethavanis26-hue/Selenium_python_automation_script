import pytest


@pytest.fixture()
def OpenBroswer():
    print("Launch the Broswer")
    print("Login the application")
    print("search the product")
    yield
    print("logout the application")