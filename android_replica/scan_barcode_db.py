# *** flipkart shipping ***

import mysql.connector
from mysql.connector import Error
from pathlib import Path
import configparser
from utils.database_config import DatabaseConfiguration


class BarcodeDB():
    def __init__(self, scanned_barcode):
        self.input_barcode = int(scanned_barcode)
        # self.data_file = "hostname.ini"
        # self.directory = "config"
        # self.config = configparser.ConfigParser()
        #
        # self.current_file_path = Path(__file__).parent.parent
        # self.actual_file_path = self.current_file_path.joinpath(self.directory).joinpath(self.data_file)
        # self.config.read(self.actual_file_path)

        # create a separate function for the db_config or better if you can create it as a utility file
        # inside until folder, this will keep the db configuration separate.

        # self.hostname = self.config['ABS_warehouse_hostname']['hostname']  # can be an url or localhost
        # self.port = self.config['ABS_warehouse_hostname']['port']
        # self.database = self.config['ABS_warehouse_hostname']['database']
        # self.username = self.config['ABS_warehouse_hostname']["username"]
        # self.password = self.config['ABS_warehouse_hostname']['password']
        self.inst = DatabaseConfiguration()
        self.connection = self.connect_db()

    # Connect to a db and verify if it's connected
    def connect_db(self):
        try:
            conn = mysql.connector.connect(host=self.inst.db_config()['host'],
                                           port=self.inst.db_config()['port'],
                                           database=self.inst.db_config()['database'],
                                           user=self.inst.db_config()['username'],
                                           password=self.inst.db_config()['password'])

            if conn.is_connected():
                return conn
        except Error as e:
            print(f"looking: {e}")
            return None

    # To verify if the barcode scanned is available in DB
    def scan_barcode(self):
        if self.connection:  # checking for connection is set up or not
            cursor = self.connection.cursor()
            cursor.execute("Select barcode from Scan_data where barcode = %s", (self.input_barcode,))
            result = cursor.fetchone()
            print("test", result)
            if result:
                return "success"
            else:
                return "failure"
        else:
            return "failure"


if __name__ == "__main__":
    input_barcode = input("enter barcode")
    scanner = BarcodeDB(input_barcode)
    print(scanner.scan_barcode())
    # connect_obj = BarcodeDB()
    # print(connect_obj.connect_db())
