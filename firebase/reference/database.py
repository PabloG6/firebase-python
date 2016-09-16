import json
import urllib.parse

from firebase.app.App.Firebase import firebase
from urllib import request

class database():
    def __init__(self, firebase):
        self.connection = firebase.connection
        self.firebase = firebase
        self.path = ''
        self.key = ''
        pass

    def ref(self, path):
        self.path = self.path + '/' + path
        print(self.path)
        return self

    def push(self, data=None):
        #convert data passed to json object
        data = json.dumps(data)
        #append the path with .json
        self.connection.request("POST", self.path+'.json', data)

        response = self.connection.getresponse()
        #get the key created
        self.key = response.read()
        print("POST", response.status, response.reason)
        return self

    def get(self):
        self.connection.request("GET", self.path+'.json')
        print(self.connection)
        response = self.connection.getresponse()
        data = response.read()
        return data

    def child(self, child):
        self.path = self.path+"/"+child
        return self

    def parent(self):
        #todo use regex expressions to strip end of the path
        pass


