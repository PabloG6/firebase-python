from http import client
from urllib import request


class firebase():
    def __init__(self, database_url):
        """"
        initializes and creates a connection to the firebase reference
        :param database_url: the reference url to be passed
        """
        # TODO change the following configuration system to config
        self.database_url = database_url
        self.connection = client.HTTPSConnection(database_url)









