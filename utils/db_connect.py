# *** flipkart shipping ***
from pathlib import Path
import configparser

# This is actually a parser file
file_name = "hostname.ini"
directory_name = "config"

config = configparser.ConfigParser()
base_directory = Path(__file__).parent.parent
file_path = base_directory.joinpath(directory_name).joinpath(file_name)

# Read the config file (.ini)
config.read(file_path)


# Parse the config file (.ini)
def get_hostname_data():
    return config['ABS_warehouse_hostname']['hostname']


def get_port_data():
    return config['ABS_warehouse_hostname']['port']


print(get_hostname_data())




