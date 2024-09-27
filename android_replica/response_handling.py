# warehouse
import codecs
from datetime import datetime

import requests

from utils.product_table_utility import ProductTableInitializer


class ProductTable:
    """
    Class to create a product table if no duplicates exists

    Method
    ------
    response_handler
        :param url_header
    """

    def __init__(self, url_header):
        initializer = ProductTableInitializer()
        self.url, self.headers = initializer.get_url_and_headers()

    def response_handler(self):
        response = requests.get(self.url, headers=self.headers)
        # response_data = StringIO(response.text)  # the data is in string format,
                                                   # need to convert it in file format TSV
        # reader = pd.read_csv(response_data, sep='\t')  # pd is from pandas


        # hash-set approach - performance efficient but not memory efficient
        processed_data = []
        seen = set()
        file_path = 'output\product_table.dat'
        no_duplicates = True

        parsed_data = response.text
        # Clean the parsed data to remove any unwanted invisible characters
        parsed_data = parsed_data.replace('\uFEFF', '').replace('\u200B', '')
        lines = parsed_data.strip().split('\n')  # type - list of rows
        for line in lines[1:-1]:
            processed_data.append(line.strip().split('\t'))  # list-of-list of row data

        for row in processed_data:
            if row[2] != '':
                key = row[2]
                if key in seen:
                    no_duplicates = False
                    return  "Duplicate barcode for Product code " + row[1]
                else:
                    seen.add(key)

        if no_duplicates:
            with codecs.open(file_path, 'w', encoding='utf-8') as product_table:
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                product_table.write(f"Date and Time: {current_datetime}\n")
                product_table.write(''.join(parsed_data))
        else:
            print("Duplicate key found. File not created.")

        return seen

if __name__ == "__main__":
    url_header = ProductTableInitializer()
    product_table = ProductTable(url_header)
    print(product_table.response_handler())
