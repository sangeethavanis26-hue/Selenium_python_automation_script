import pytest


def testLogin():
    print("Login Successful")

@pytest.mark.smoke
def testLogout():
    print("Logout Successful")

def testCalculation():
   assert 2+2 == 4

