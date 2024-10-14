# TYPES AND CLASS DEFINITION AND/OR MODIFICATION
import datetime
import pymongo
import pymongo.collection

class Person:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
    def get_string(self):
        return self.first_name + " " + self.family_name
    
class Query:
    def get_query(self):
        query = {}
        for argument in self.__dict__:
            if getattr(self, argument) != None:
                query[argument] = getattr(self, argument)
        return query

class Readquery(Query):
    def __init__(self, owner : Person = None , due_date : datetime.datetime = None,):
        Query.__init__()
        self.due_date = due_date
        self.owner = owner
    def send_query(self, collection : pymongo.collection):
        collection.find(self.get_query())

class Writequery(Query):
    def __init__(self, title : str, owner : Person = None , due_date : datetime.datetime = None,):
        Query.__init__()
        self.title = title
        self.due_date = due_date
        self.owner = owner
    def send_query(self, collection : pymongo.collection):
        collection.insertOne(self.get_query())

    

    

#LIRE > personne et/ou date
#ECRIRE > titre + date (optionnel) + personne (optionnel)
#MODIFIER > ID + date et/ou personne
#SUPPRIMER > ID