#This file contains the interface with the database
import pymongo
from lib import common_types
import datetime

class DataBaseManager:
    def __init__(self):
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client.todolist
        self.tasks_collection = self.db.tasks
        self.users_collection = self.db.users
    
    def read(self, query : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find(query)
    
    def write(self, query : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.insert_one(query)


            