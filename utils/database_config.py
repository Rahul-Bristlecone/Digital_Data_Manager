# *** flipkart shipping ***
#  this is a utility to fetch and configure database from the config file (.ini)
#  __init__ will fetch the config file (.ini) and
#  db_config will configure the database with the values provided in config (.ini) file

from pathlib import Path
import configparser


class DatabaseConfiguration:
    """
    class responsible for managing DB configuration for further use

    Method
    ------
    db_config

    """
    config_file = "hostname.ini"
    config_directory = "config"
    config = configparser.ConfigParser()

    def __init__(self):
        self.current_directory = Path(__file__).parent.parent
        self.config_file_path = self.current_directory.joinpath(self.config_directory).joinpath(self.config_file)

        # parse this file using configparser
        self.config.read(self.config_file_path)

    def db_config(self):
        mc_connection = {'host': self.config['MC3000 server']['hostname'],
                         'port': self.config['MC3000 server']['port'],
                         }

        mysql_connection = {'host': self.config['MYSQL connection']['host'],
                            'port': self.config['MYSQL connection']['port'],
                            'database': self.config['MYSQL connection']['database'],
                            'username': self.config['MYSQL connection']['username'],
                            'password': self.config['MYSQL connection']['password']
                            }

        return mc_connection, mysql_connection
