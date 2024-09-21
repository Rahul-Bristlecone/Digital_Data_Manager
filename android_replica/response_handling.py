import configparser

import requests
from pathlib import Path


class ProductTable():
    file_name = "hostname.ini"
    directory_name = "config"
    config =configparser.ConfigParser()

    def __init__(self):
        self.parent_path = Path(__file__).parent.parent
        self.original_file = self.parent_path.joinpath(self.directory_name).joinpath(self.file_name)

    def setup_connection(self):
        hostname = self.config.read(self.original_file)["ABS_warehouse_hostname"]["hostname"]
        port = self.config.read(self.original_file)["ABS_warehouse_hostname"]["port"]
        endpoint = "/PRODUCTS"
        url = "http://" + hostname + ":" + port + endpoint

        headers = {
            "user_agent": "AbsScan/1.09"
        }

        response = requests.get(url, headers=headers)

        return response


if __name__ == "__main__":
    obj = ProductTable()
    print(obj.setup_connection())

