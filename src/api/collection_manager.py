import pymongo
import pymongo.results
import pymongo.collection
import pymongo.database
import pymongo.errors
import pymongo.cursor


class CollectionManager:
    def __init__(self):
        self.collection = None
    def find(self,filter):
        return self.collection.find(filter)
    def find_one(self, filter):
        return self.collection.find_one(filter)
    def update(self, id, updates):
        return self.collection.update_one({"_id": id}, updates)
    def delete(self, id):
        return self.collection.delete_one({"_id": id})
    def write(self, document : dict):
        return self.collection.insert_one(document)

class TaskCollectionManager(CollectionManager):
    def __init__(self, database : pymongo.database.Database):
        CollectionManager.__init__(self)
        self.collection = database['tasks']
    def count(self, filter=None):
        return self.collection.count_documents(filter or {})

class CollaboratorCollectionManager(CollectionManager):
    def __init__(self, database : pymongo.database.Database):
        CollectionManager.__init__(self)
        self.collection = database['collaborators']
    def get_id(self, name : dict):
        return self.collection.find_one({"name" : name}).get("_id", None)
    def get_name(self, id : dict):
        return self.collection.find_one({"_id" : id}).get("name", None)
    def get_role(self, collaborator : dict):
        return self.collection.find_one(collaborator).get("role", None)

