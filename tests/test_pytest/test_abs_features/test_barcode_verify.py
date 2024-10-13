# warehouse
import json
import pytest
from android_replica.scan_barcode import ScanBarcode

# read the json
# @pytest.fixture(scope="module")
def barcodes():
    with open ("D:\\Rahul\\Projects\\Digital Data Manager\\Source code\\Digital_Data_Manager\\android_replica\\resources\\barcodes.json") as f:
        data = json.load(f)
    return data

# existing barcode scan - success
@pytest.mark.parametrize("barcode", barcodes()["barcodes_success"])
def test_barcode_success(barcode):
    test_obj = ScanBarcode(barcode)
    result, status = test_obj.scanned_barcode_verify()
    assert status == "success"


@pytest.mark.parametrize("barcode", barcodes()["barcodes_failure"])
def test_barcode_failure(barcode):
    test_obj = ScanBarcode(barcode)
    result, status = test_obj.scanned_barcode_verify()
    assert status == "failure"


if __name__ == "__main__":
    pytest.main()
