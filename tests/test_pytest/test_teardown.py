# fixtures are like before test - it might include DB connections and selenium drivers
import os

import pytest


# task: write a fixture to test if a list has been appended


def test_append_list(append_list):
    append_list.pop()
    assert append_list == pytest.lst1


def test_len_check(append_list):
    append_list.pop()
    assert len(append_list) == len(pytest.lst1)


# Tear Down example on file operations
# Open a file from the fixture, do your operations
# (in test function) assert the operation has been done.
# close the file and delete when test is done
# code after the clean-up code or tear down
@pytest.fixture()
def file_data():
    with open("test_data.txt", 'w') as new:
        new.write("This is good and practical")
        new.close()
    with open("test_data.txt", "r") as readonly:
        yield readonly

    os.remove("test_data.txt")


def test_file_operation(file_data):
    assert (file_data.readline()) == "This is good and practical"

# Sharing fixtures - kind of plugin using conftest.py - it needs not be imported,
# should be available to other tests by default
