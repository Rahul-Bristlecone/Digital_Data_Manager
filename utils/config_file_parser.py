import configparser
from pathlib import Path


# Object-oriented way of parsing the data from the confiq file

class ConfigParser():
    file_name = "hostname.ini"
    directory_name = "config"
    config = configparser.ConfigParser()

    def __init__(self, cfg=file_name):
        self.cfgfile = cfg
        self.base_file = Path(__file__).parent.parent
        self.file_path = self.base_file.joinpath(self.directory_name).joinpath(self.file_name)
        self.config.read(self.file_path)

    def get_hostname_data(self):
        return self.config['ABS_warehouse_hostname']['hostname']

    def get_port_data(self):
        return self.config['ABS_warehouse_hostname']['port']


if __name__ == '__main__':
    conf = ConfigParser() # by default, it will pick hostname.ini
    print(conf.get_port_data())
    print(conf.get_hostname_data())
