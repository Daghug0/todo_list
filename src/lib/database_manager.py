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
    
    def read(self, filter : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find(filter)
    
    def write(self, query : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.insert_one(query)

    def modify(self, filter, updates : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.update_one(filter, updates)
    
    def delete(self, filter : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.delete_one(filter)

    def is_present(self, filter) -> bool:
        return (len(self.tasks_collection.find_one(filter))!=0)

    def find_one(self,filter) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find_one(filter)


            