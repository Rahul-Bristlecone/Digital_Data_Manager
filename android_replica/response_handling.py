import configparser

import requests
import csv
from pathlib import Path
from io import StringIO
import pandas as pd
from select import error


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
        response_data = StringIO(response.text)
        reader = pd.read_csv(response_data, sep='\t')

        if reader['6'].duplicated().any():
            print("could not save due to duplicated data")

        else:
            reader.to_csv("/new.dat", sep="\t", index=False)

        return reader


if __name__ == "__main__":
    obj = ProductTable()
    print(obj.setup_connection())
