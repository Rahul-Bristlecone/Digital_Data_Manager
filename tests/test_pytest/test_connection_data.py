from utils.hostname_reader import *


def test_connection():
    hostname = get_hostname_data()
    port = get_port_data()


# now you have got data.
# Use this data to test if successful connection is being made or not.
# There will be a function will set up connection and check the response.
# This function will be appending hostname & port to set up connection.