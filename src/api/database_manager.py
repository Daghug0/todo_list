#This file contains the interface with the database
import pymongo
import pymongo.results
import pymongo.collection
import pymongo.database
import pymongo.errors
import pymongo.cursor

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
        #First part of the function allow to find the collaborator_id based on his name
        final_filter = self.replace_collaborator_name_by_id(filter)
        #After replacing collaborator_name by is ID, we can search the task
        return self.tasks_collection.find(final_filter)
    
    def write_task(self, task : dict) -> pymongo.cursor.CursorType:
        final_task = self.replace_collaborator_name_by_id(task)
        if final_task ==None:
            return None
        else:
            return self.tasks_collection.insert_one(task)

    def modify_task(self, task_id : str, updates : dict) -> pymongo.results.UpdateResult:
        return self.tasks_collection.update_one(task_id, updates)
    
    def delete_task(self, task_id : str) -> pymongo.cursor.CursorType:
        return self.tasks_collection.delete_one(task_id)

    #maybe redundant with read_tasks()
    def is_task_present(self, filter) -> bool:
        return (len(self.tasks_collection.find_one(filter))!=0)

    #maybe useless
    def find_one_task(self,filter) -> pymongo.cursor.CursorType:
        return self.tasks_collection.find_one(filter)
    
    def get_collaborator_document(self, collaborator_id : str) -> dict:
        return self.collaborators_collection.find_one({"_id": collaborator_id})
    
    def get_collaborator_id(self, collaborator_name: dict) -> str | None:
        """
        Retrieve the collaborator's ID from the database based on the provided collaborator name.

        Parameters:
        collaborator_name (dict): A dictionary containing the name of the collaborator.

        Returns:
        str: The ID of the collaborator. If the collaborator is not found, returns None.
        """
        return self.collaborators_collection.find_one({"name": collaborator_name}).get("_id", None)
    
    def link_collaborator_to_task(self, task: dict, collaborator_name: dict) -> pymongo.results.UpdateResult | None:
        """
        Links a collaborator to a task by updating the task with the collaborator's ID.

        Parameters:
        task (dict): A dictionary representing the task to be updated.
        collaborator_name (dict): A dictionary containing the name of the collaborator to be linked to the task.

        Returns:
        pymongo.results.UpdateResult: The result of the update operation if the collaborator is found and linked.
        None: If the collaborator is not found.
        """
        collaborator_id = self.get_collaborator_id(collaborator_name)
        if collaborator_id != None:
            return self.modify_task(task, {"collaborator_id": collaborator_id})
        else:
            return None
        
    def replace_collaborator_name_by_id(self, document: dict) -> dict | None:
        #First part of the function allow to find the collaborator_id based on his name
        if "collaborator_name" in document.keys():
            collaborator_id = self.get_collaborator_id(document["collaborator_name"])
            if collaborator_id != None:
                document["collaborator_id"] = collaborator_id
            else: return None
            document.pop("collaborator_name")
        return document

    

        



            