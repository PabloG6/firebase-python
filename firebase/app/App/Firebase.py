import http
import urllib
from http import client
from urllib import request


class firebase():
    def __init__(self, database_url, api_key=None, auth_domain=None, storage_bucket=None):
        # TODO change the following configuration system to config
        """
        :param api_key: unique api key of user
        :param auth_domain: <PROJECT_ID>.firebaseapp.com
        :param database_url: <DATABASE_NAME>.firebaseio.com
        :param storage_bucket: <BUCKET>.appspot.com"
        """
        self.api_key = api_key
        self.auth_domain = auth_domain
        self.database_url = database_url
        self.storage_bucket = storage_bucket

    def initialize_app(self):
        config = {"apiKey": self.api_key,
                  "authDomain": self.auth_domain,
                  "databaseURL": self.database_url,
                  "storageBucket": self.storage_bucket
                  }
        connection = request.urlopen(self.database_url)
        print(connection)

        # return the connection variable
        return firebase


firebase = firebase("https://testing-6aa1e.firebaseio.com/",
                    api_key="python-firebase-e17d0.firebaseapp.com")
firebase.initialize_app()


