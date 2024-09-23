# mocking and patching using pytest
# as we are not using a separate db for testing, we will be using the mocking in this case
# mocking simulate the behaviour of DB and other external objects
# objects like cursor, fetch(all/one) are used to interacts with the DB

import pytest
from android_replica.scan_barcode_db import BarcodeDB


class MockCursor:
    # this class will simulate that the barcodes are already in the DB
    # only then other DB operations can be mocked
    def __init__(self, barcodes):
        self.barcodes = barcodes

    def execute(self, query, params):
        self.query = query
        self.params = params
        print(f"query: {query} and params: {params}")

    def fetchone(self):
        print(f"Fetching one with params: {self.params}")
        if self.params[0] in self.barcodes:
            print(f"Barcode {self.params[0]} found in mock database.")
            return (self.params[0],)
        print(f"Barcode {self.params[0]} not found in mock database.")
        return None

class MockConnection:
    def __init__(self, barcodes):
        self.barcodes = barcodes

    def cursor(self):
        return MockCursor(self.barcodes)

    def is_connected(self):
        return True


def test_barcode_success(mocker):
    mocker.patch('android_replica.scan_barcode_db.BarcodeDB.connect_db',
                 return_value=MockConnection([8982, 1434242, 434224]))
    scanner = BarcodeDB(8982)
    result = scanner.scan_barcode()
    print(f"Test result: {result}")
    assert scanner.scan_barcode() == "success"


def test_barcode_failure(mocker):
    mocker.patch('android_replica.scan_barcode_db.BarcodeDB.connect_db',
                 return_value=MockConnection(["232132", "14324342", "4342424"]))
    scanner = BarcodeDB("2216732")
    assert scanner.scan_barcode() == "failure"


def test_connect_db_failure(mocker):
    # Patch the connect_db method to simulate a connection failure
    mocker.patch('android_replica.scan_barcode_db.BarcodeDB.connect_db', return_value=None)
    scanner = BarcodeDB("12345")
    assert scanner.scan_barcode() == "failure"


if __name__ == "__main__":
    pytest.main()