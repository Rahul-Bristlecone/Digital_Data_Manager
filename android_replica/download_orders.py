# warehouse
import requests
from get_orders import GetOrders
from utils.product_table_utility import ProductTableInitializer


# fetch orderId from response
def order_id_from_response():
    order_ids = set()
    get_order_inst = GetOrders()
    order_list = get_order_inst.fetch_outstanding_orders().strip().split('\n')
    for list_of_orders in order_list:
        order_detail = list_of_orders.strip().split('\t')
        order_ids.add(order_detail[1])

    return order_ids


class DownloadOrders:
    def __init__(self):
        self.file_path = "output/download_orders.dat"
        self.table_inst = ProductTableInitializer()
        self.url, self.headers = self.table_inst.get_url_and_headers("downloads")

    # fetch orderId from response

    # fetch orderId from file
    def order_id_from_file(self):
        pass


    def downloaded_orders_details(self):
        open(self.file_path, 'w').close()
        for order_id in order_id_from_response():
            new_url = f"{self.url}/{order_id}"
            response = requests.get(new_url, headers=self.headers)

            with open(self.file_path, 'a') as download_file:
                download_file.write(response.text)

        return response.status_code

if __name__ == "__main__":
    download_order_inst = DownloadOrders()
    print(order_id_from_response())
    print(download_order_inst.downloaded_orders_details())