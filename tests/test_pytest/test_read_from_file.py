import pytest
from utils.util import read_data


# This time data in parameter is being supplied from the data file
new_list = []
# As the data is in column form, so a,b,c,d denote column name
@pytest.mark.parametrize("a,b,c,d", read_data())
def test_read_data(a,b,c,d):
    assert b
    new_list.append(b)