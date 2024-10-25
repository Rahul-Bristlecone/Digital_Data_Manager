# *** flipkart shipping ***
import mysql.connector
from mysql.connector import Error

from utils.database_config import DatabaseConfiguration


class BarcodeDB:
    def __init__(self, scanned_barcode):
        self.input_barcode = int(scanned_barcode)
        self.inst = DatabaseConfiguration()
        self.connection = self.connect_db()  # To setup db connection

    # Connect to db and verify if it's connected
    def connect_db(self):
        mc_inst, mysql_inst = self.inst.db_config()
        try:
            conn = mysql.connector.connect(host=mysql_inst['host'],
                                           port=mysql_inst['port'],
                                           database=mysql_inst['database'],
                                           user=mysql_inst['username'],
                                           password=mysql_inst['password'])

            if conn.is_connected():
                return conn
        except Error as e:
            print(f"looking: {e}")
            return None

    # To verify if the barcode scanned is available in DB
    def scan_barcode(self):
        if self.connection:  # checking for connection is set up or not
            cursor = self.connection.cursor()
            cursor.execute("Select * from product_table where barcode = %s",
                           (self.input_barcode,))
            result = cursor.fetchone()
            if result:
                prod_code, prod_desc, barcode = result
                return {
                        "encoding": len(barcode),
                        "product code": prod_code,
                        "Description": prod_desc,
                        "Barcode": barcode
                        }
            else:
                return {"Barcode" : self.input_barcode}
        else:
            return "connection set-up failed"


if __name__ == "__main__":
    input_barcode = input("Enter/Scan barcode")
    scanner = BarcodeDB(input_barcode)
    print(scanner.scan_barcode())
    # connect_obj = BarcodeDB()
    # print(connect_obj.connect_db())
