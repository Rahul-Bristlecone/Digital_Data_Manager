# warehouse
import requests
from get_orders import GetOrders
from utils.product_table_utility import ProductTableInitializer


class DownloadOrders:
    def __init__(self):
        self.file_path = "output/download_orders.dat"
        self.table_inst = ProductTableInitializer()
        self.url, self.headers = self.table_inst.get_url_and_headers("downloads")
        self.order_ids = self.order_id_from_response()


    # fetch orderId from response
    @staticmethod  # static method does not require an instance to call it
    def order_id_from_response():
        order_ids = set()
        get_order_inst = GetOrders()
        order_list = get_order_inst.fetch_outstanding_orders().strip().split('\n')
        for list_of_orders in order_list:
            order_detail = list_of_orders.strip().split('\t')
            order_ids.add(order_detail[1])

        return order_ids

    # fetch orderId from file
    def order_id_from_file(self):
        pass


    def downloaded_orders_details(self):
        open(self.file_path, 'w').close()
        response = None

        for order_id in self.order_ids:
            new_url = f"{self.url}/{order_id}"
            try:
                response = requests.get(new_url, headers=self.headers)
                response.raise_for_status()
            except requests.RequestException as e:
                print("error fetching data for order id ",order_id , e)
                continue

            with open(self.file_path, 'a') as download_file:
                download_file.write(response.text)

        return response.status_code if response else None

if __name__ == "__main__":
    download_order_inst = DownloadOrders()
    print(download_order_inst.downloaded_orders_details())