# warehouse
from utils.file_parser import FileParser

class ProductTableInitializer:
    def __init__(self):
        self.file_parser = FileParser()
        self.fetch = self.file_parser.config
        self.file_parser.file_path()


    def get_url_and_headers(self):
        hostname = self.fetch["ABS_warehouse_hostname"]["hostname"]
        port = self.fetch["ABS_warehouse_hostname"]["port"]
        endpoint = "/PRODUCTS"
        url = "http://" + hostname + ":" + port + endpoint
        headers = {
            "User-Agent": "AbsScan/1.09"
        }

        return url, headers