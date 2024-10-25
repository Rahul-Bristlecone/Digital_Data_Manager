# warehouse
from datetime import datetime

import codecs

from utils.product_table_utility import ProductTableInitializer
import requests
import os


class GetOrders:
    def __init__(self):
        data = ProductTableInitializer()
        self.url, self.header = data.get_url_and_headers("orders")

    def fetch_outstanding_orders(self):
        response = requests.get(self.url, headers=self.header)

        file_path = "output\orders_list.dat"
        with codecs.open(file_path, 'w') as order_table:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            order_table.write(f"Date and Time: {current_datetime}\n")
            order_table.write(''.join(response.text))

        return response.text

if __name__ == "__main__":
    inst = GetOrders()
    inst.fetch_outstanding_orders()
