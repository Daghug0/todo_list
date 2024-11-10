#This file contains the interface with the database
import pymongo
import pymongo.results
import pymongo.collection
import pymongo.database
import pymongo.errors

class DataBaseManager:
    def __init__(self):
        self.client = None
        self.db = None
        self.tasks_collection = None
        self.collaborators_collection = None
        
        try:
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client['todolist']  # Correct way to access the database
            self.tasks_collection = self.db['tasks']
            self.collaborators_collection = self.db['collaborators']
        except (pymongo.errors.ConnectionFailure,pymongo.errors.InvalidName) as e:
            self.close()
            raise SystemExit(e)
        
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
    
    def close(self):
        if self.client and self.client.is_primary:
            self.client.close()
    
    def read_tasks(self, filter : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find(filter)
    
    def write_task(self, query : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.insert_one(query)

    def modify_task(self, filter, updates : dict) -> pymongo.results.UpdateResult:
        return self.tasks_collection.update_one(filter, updates)
    
    def delete_task(self, filter : dict) -> pymongo.cursor.CursorType:
        return self.tasks_collection.delete_one(filter)

    def is_task_present(self, filter) -> bool:
        return (len(self.tasks_collection.find_one(filter))!=0)

    def find_one_task(self,filter) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find_one(filter)
    
    def find_collaborator(self, collaborator_filter):
        return self.collaborators_collection.find_one(collaborator_filter)
    
    def is_collaborator_present(self, filter) -> bool:
        return (len(self.collaborators_collection.find_one(filter))!=0)
    
    def link_collaborator_to_task(self, task, collaborator_name):
        if self.is_collaborator_present(collaborator_name):
            collaborator_object = self.find_collaborator(collaborator_name)
            return self.modify_task(task, {"collaborator" : collaborator_object["_id"]}) 
        
    

        



            