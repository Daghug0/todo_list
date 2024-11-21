#This file contains the interface with the database
import pymongo
import pymongo.results
import pymongo.collection
import pymongo.database
import pymongo.errors
import pymongo.cursor

from .collection_manager import TaskCollectionManager, CollaboratorCollectionManager

class DataBaseManager:
    def __init__(self):
        self.client = None
        self.db = None
        self.tasks_collection = None
        self.collaborators_collection = None
        
        try:
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client['todolist']  # Correct way to access the database
            self.tasks = TaskCollectionManager(self.db)
            self.collaborators = CollaboratorCollectionManager(self.db)
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
        if "due_date" in filter.keys():
            filter["due_date"] = {"$lt" : filter["due_date"]}
        filter = self.replace_collaborator_name_by_id(filter)
        return self.tasks.find(filter)  
    def write_task(self, task_with_name : dict) -> pymongo.cursor.CursorType:
        task = self.replace_collaborator_name_by_id(task_with_name)
        result_write = self.tasks.write(task)
        if result_write.acknowledged:
            return self.read_tasks({"_id": result_write.inserted_id})
        else :
            raise SystemExit("Failed to insert task, aborting...")
    def modify_task(self, task_id : dict, updates : list) -> pymongo.results.UpdateResult:
        return self.tasks.update(task_id, updates)
    def count_task(self, filter):
        return self.tasks.count(filter)
    def delete_task(self, task_id : dict):
        return self.tasks.delete(task_id)
        
    def replace_collaborator_name_by_id(self, document: dict) -> dict | None:
        if "collaborator_name" in document.keys():
            collaborator_id = self.collaborators.get_id(document["collaborator_name"])
            if collaborator_id != None:
                document["collaborator_id"] = collaborator_id
            else:
                raise ValueError("Collaborator not found")
            document.pop("collaborator_name")
        return document

    

        



            