import configparser

import requests
import os
import csv
from pathlib import Path
from io import StringIO
import pandas as pd
from select import error

from utils.hostname_reader import file_path


class ProductTable():
    file_name = "hostname.ini"
    directory_name = "config"
    config = configparser.ConfigParser()

    def __init__(self):
        self.parent_path = Path(__file__).parent.parent
        self.original_file = self.parent_path.joinpath(self.directory_name).joinpath(self.file_name)
        self.config.read(self.original_file)

        hostname = self.config["ABS_warehouse_hostname"]["hostname"]
        port = self.config["ABS_warehouse_hostname"]["port"]
        endpoint = "/PRODUCTS"
        self.url = "http://" + hostname + ":" + port + endpoint
        self.headers = {
            "User-Agent": "AbsScan/1.09"
        }

    def setup_connection(self):
        response = requests.get(self.url, headers=self.headers)
        parsed_data = response.text
        # response_data = StringIO(response.text)  # the data is in string format, need to convert it in file format TSV
        # reader = pd.read_csv(response_data, sep='\t')

        # if reader['6'].duplicated().any():
        #     print("could not save due to duplicated data")  # data available is not nice
        #
        # else:
        #     reader.to_csv("/new.dat", sep="\t", index=False)

        # this is a hash-set approach - efficient but not memory efficient
        lines = parsed_data.strip().split('\n')  # type - list of rows
        print(lines)
        processed_data = []
        no_duplicates = True
        for line in lines[1:len(lines)-1]:
            processed_data.append(line.strip().split('\t'))  # list-of-list of row data

        print(processed_data)

        # output_dir = '/output'
        # file_path = os.path.join(output_dir, '/product_table.dat')
        # print(file_path)
        seen = set()
        file_path = 'output\product_table.dat'

        for row in processed_data:
            if row[2] != '':
                key = row[2]
                if key in seen:
                    no_duplicates = False
                    return "False"
                else:
                    seen.add(key)

        if no_duplicates:
            with open(file_path, 'w') as product_table:
                product_table.write(''.join(parsed_data))
        else:
            print("Duplicate key found. File not created.")

        print(seen)
        # return response.text


if __name__ == "__main__":
    obj = ProductTable()
    print(obj.setup_connection())
