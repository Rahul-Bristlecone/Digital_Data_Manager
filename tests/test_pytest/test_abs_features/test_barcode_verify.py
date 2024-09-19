import json
from pathlib import Path
import pytest
from android_replica.scan_barcode import ScanBarcode


# this is a test set-up (replace it with data driven testing)
# @pytest.fixture(scope="module", autouse=True)
# def set_up():
#     barcode_data = {
#         "barcodes": ["2424343242", "1234567890", "0987654321"]
#     }
#
#     file_name = "barcodes.json"
#     directory_name = "android_replica\\resources"
#
#     base_directory = Path(__file__).parent.parent.parent.parent
#     file_path = base_directory.joinpath(directory_name).joinpath(file_name)
#     print(file_path)
#     with open(file_path, 'w') as f:
#         json.dump(barcode_data, f)


# existing barcode scan - success
def test_barcode_success():
    test_obj = ScanBarcode("2424343242")
    result = test_obj.scan_barcode()
    print(f"Test success result: {result}")  # Debug statement
    assert result == "success"


# some other barcode scan - failure
def test_barcode_failure():
    scanner = ScanBarcode("1111111111")
    result = scanner.scan_barcode()
    print(f"Test failure result: {result}")
    assert result == "failure"


if __name__ == "__main__":
    pytest.main()
