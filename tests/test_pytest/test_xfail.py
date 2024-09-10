# this is supposed to run and supposed to fail to test if negative test scenarios
# are handled by the code
import sys

import pytest


# xfail for pre-test conditions & negative test cases
# if you expect a test to fail, better use xfail
@pytest.mark.xfail(raises=TypeError)
@pytest.mark.xfail(sys.platform == "win64", reason="known issue on android")
def test_os_verify():
    letters = "abcd"
    numbers = 1234
    assert letters + numbers == "abcd1234"



# fixtures are like before test & after test tests
# like test browsers, db connections - use cases
# fixture is actually passed as argument in a test function - one way to call the fixture
# another is using a marker
@pytest.fixture()
def store_data():
    print("***** Testing fixtures *****")
    data = ["store_id", "store_name", "tags", "products included"]
    return data

def test_create_store(store_data):
    assert store_data[0:2] == ["store_id", "store_name"]


def reverse_list(lst):
    lst.reverse()
    return lst


def test_reverse_list(store_data):
    assert store_data[::-1] == reverse_list(store_data) # return value is a list from store_data


# return value from fixture cannot be used in this case
@pytest.mark.usefixtures("store_data")
def test_fixture_demo():
    assert 1 == 1
    assert store_data() == ["store_id", "store_name", "tags", "products included"]

