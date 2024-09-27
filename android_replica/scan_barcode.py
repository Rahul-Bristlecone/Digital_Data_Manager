# barcodes are stored in json file or in DB
# New barcode is scanned or entered as input
import json
import os
from pathlib import Path


class ScanBarcode:
    """
    Class to scan & verify barcode from product table

    Method
    ------
    scanned_barcode_verify
        :param None
    """

    # New barcode is scanned or entered as input
    def __init__(self, barcode):
        self.input_barcode = barcode
        print(f"Initialized with barcode: {self.input_barcode}")

    # barcodes are stored in json file or in DB
    # as DB is now available in .dat file then compare with the barcode
    # in product_table.dat file
    def scanned_barcode_verify(self):
        file_name = "barcodes.json"  # try with .dat file later
        directory_name = "android_replica\\resources"

        base_directory = Path(__file__).parent.parent
        file_path = base_directory.joinpath(directory_name).joinpath(file_name)

        if os.path.exists(file_path):
            with open(file_path, 'r') as barcode_file:
                try:
                    read_barcodes = json.load(barcode_file)  # returns a dict
                    if self.input_barcode in read_barcodes.get("barcodes", []):
                        return True
                    # scan_barcode and product table are interrelated
                    else:
                        return False
                except json.JSONDecodeError:
                    print(f"Error: {file_path} is not a valid JSON file.")


if __name__ == '__main__':
    user_input = input("Enter Barcode: ")
    scanner = ScanBarcode(user_input)
    if scanner.scanned_barcode_verify():
        print("Successful scan")
    else:
        print("Product do not exist in DB")
