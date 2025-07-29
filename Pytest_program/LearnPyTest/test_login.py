import pytest


@pytest.mark.smoke
def testLogin():
    print("Login Successful")
@pytest.mark.skip
# @pytest.mark.sanity
def testLogout():
    print("Logout Successful")
@pytest.mark.xfail
def testCalculation():
   assert 2+2 == 6

