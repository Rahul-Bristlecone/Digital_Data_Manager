import pytest


def pytest_configure():
    pytest.lst1 = [12, 13, 12, 98, 1, 26]


@pytest.fixture()
def append_list():
    list1 = pytest.lst1
    list1.append(56)
    yield list1
    print("Driver syncing")
