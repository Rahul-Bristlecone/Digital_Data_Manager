# barcodes are stored in json file or in DB
# New barcode is scanned or entered as input
import json
import os
from pathlib import Path


# barcode_list = []
# file_path = "resources/barcodes.json"
# if os.path.exists(file_path):
#     with open(file_path, 'r') as barcodes:
#         try:
#             barcode_list = json.load(barcodes)
#             print("Loaded barcodes:", barcode_list)  # Debug statement
#         except json.JSONDecodeError:
#             print(f"Error: {file_path} is not a valid JSON file.")


class ScanBarcode():

    # New barcode is scanned or entered as input
    def __init__(self, barcode):
        self.input_barcode = barcode
        print(f"Initialized with barcode: {self.input_barcode}")

    # barcodes are stored in json file or in DB
    def scan_barcode(self):
        file_name = "barcodes.json"
        directory_name = "android_replica\\resources"

        base_directory = Path(__file__).parent.parent
        file_path = base_directory.joinpath(directory_name).joinpath(file_name)
        print(file_path)

        # store_barcode = []
        with open(file_path, 'r') as barcode_file:
            read_barcodes = json.load(barcode_file)  # returns a dict
            # store_barcode.append(read_barcodes)
        print(read_barcodes)
        if self.input_barcode in read_barcodes.get("barcodes", []):
            return "success"
        else:
            return "failure"


if __name__ == '__main__':
    user_input = input("Enter Barcode: ")
    scanner = ScanBarcode(user_input)
    print(scanner.scan_barcode())
