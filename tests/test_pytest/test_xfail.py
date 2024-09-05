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
