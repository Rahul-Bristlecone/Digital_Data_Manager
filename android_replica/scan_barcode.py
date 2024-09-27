# warehouse
from pathlib import Path
import os

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

    # Earlier Json, now DB is now available in .dat file then compare with the barcode
    # in product_table.dat file
    def scanned_barcode_verify(self):
        # file_name = "barcodes.json"  # try with .dat file later
        # directory_name = "android_replica\\resources"

        file_name = "product_table.dat"
        directory_name = "android_replica\\output"

        base_directory = Path(__file__).parent.parent
        file_path = base_directory.joinpath(directory_name).joinpath(file_name)

        # without the use of a new variable for flag
        if os.path.exists(file_path):
            with open(file_path, 'r') as product_table:
                for _ in range(2):
                    next(product_table)

                for line in product_table:
                    barcodes = line.strip().split('\t')
                    if barcodes[2] == self.input_barcode:
                        product_detail = {"Barcode" : barcodes[2],
                                          "encoding" : "utf-8",
                                          "Product code" : barcodes[1],
                                          "Product description" : barcodes[3]
                                         }
                        return product_detail
                else:
                    return self.input_barcode

if __name__ == '__main__':
    user_input = input("Enter Barcode: ")
    scanner = ScanBarcode(user_input)
    print(scanner.scanned_barcode_verify())

