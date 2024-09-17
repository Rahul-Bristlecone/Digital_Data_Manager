# this util.py is used to read data from config/data.csv file
# data driven testing
import csv
from pathlib import Path

data_file  =  "data.csv"
data_directory = "config"

# Path(__file__) denotes the path of current working file
base_directory = Path(__file__).parent.parent
data_file_path = base_directory.joinpath(data_directory).joinpath(data_file)


def read_data():
    with open(data_file_path, "r") as test_data:
        reader = csv.reader(test_data)
        next(reader) # skips the first row
        data_from_csv = [tuple(row) for row in reader]
    return data_from_csv

