import pytest
import configparser
from utils.config_file_parser import ConnectionDataParser

# this is following the OOPs model which is a good practice

conf = ConnectionDataParser('hostname.ini')


def test_hostname():
    print(conf.get_hostname_data())


def test_port():
    print(conf.get_port_data())
