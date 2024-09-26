from abc import abstractmethod
from http.client import responses

from database import database

class user:
    def __init__(self,email,password):
        self.email = email
        self.password = password


    def login(self,email,password):
        response =  database.seekUser(email,password)
        if response == 'No':
            print('User Not Found')
        else:
            self.role = response