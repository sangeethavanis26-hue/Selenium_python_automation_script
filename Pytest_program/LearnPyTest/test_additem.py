import pytest


def testLogin():
    print("Login Successful")

def testLogout():
    print("Logout Successful")

@pytest.mark.smoke
def testCalculation():
   assert 2+2 == 4

# LearnPyTest\test_login.py -vsk log