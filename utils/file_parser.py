# Warehouse
import configparser
from pathlib import Path

class FileParser:
    """
    Class to parse the content of configuration file

    Method
    ------
    file_path()
        :param None
    """

    def __init__(self):
        self.config_file = "hostname.ini"
        self.config_directory = "config"
        self.current_directory = Path(__file__).parent.parent
        self.config_file_path = self.current_directory.joinpath(self.config_directory).joinpath(self.config_file)
        self.config = configparser.ConfigParser()

    def file_path(self):
        # parse this file using configparser
        return self.config.read(self.config_file_path)


if __name__ == "__main__":
    obj = FileParser()
    print(obj.file_path())