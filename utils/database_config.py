#  this is a utility to fetch and configure database from the config file (.ini)
#  __init__ will fetch the config file (.ini) and
#  db_config will configure the database with the values provided in config (.ini) file

from pathlib import Path
import configparser


class DatabaseConfiguration():
    config_file = "hostname.ini"
    config_directory = "config"
    config = configparser.ConfigParser()

    def __init__(self, cfg=config_file):
        self.cfg_file = cfg
        self.current_directory = Path(__file__).parent.parent
        self.config_file_path = self.current_directory.joinpath(self.config_directory).joinpath(self.config_file)

        # parse this file using configparser
        self.config.read(self.config_file_path)

    def db_config(self):
        db_data = {'host': self.config['ABS_warehouse_hostname']['hostname'],
                   'port': self.config['ABS_warehouse_hostname']['port'],
                   'database': self.config['ABS_warehouse_hostname']['database'],
                   'username': self.config['ABS_warehouse_hostname']['username'],
                   'password': self.config['ABS_warehouse_hostname']['password']
                   }

        return db_data
