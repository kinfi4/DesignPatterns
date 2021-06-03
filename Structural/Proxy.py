from random import random


class DataBase:
    """ This is heavy object, we dont want to create with no purpose """

    def make_request(self, sql='SELECT * FROM DATABASE;'):
        print(f'Making some request with {sql}')


class ProxyDB(DataBase):
    """ The idea of database proxy is that we create database instance only if its needed """

    def __init__(self):
        self.data_base = None

    def make_request(self, sql='SELECT * FROM DATABASE;'):
        if self.data_base_is_available():
            self.data_base = DataBase()
            self.data_base.make_request(sql)
        else:
            print('Not available')

    @staticmethod
    def data_base_is_available():
        return random() < 0.5


db = ProxyDB()
db.make_request()  # So that we build connection only when db is available
db.make_request()
db.make_request()
db.make_request()
