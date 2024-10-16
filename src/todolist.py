#!bin/python3

#This file run our application and contains the interface for the user to enter his command

from pymongo import MongoClient
from lib import display,date_translation,user_interface,common_types
import datetime
import string

#This function find tasks in mongoDB based on user command
# Input     : UserCommand object
# Output    : Cursor of mongoDB documents containing requested tasks
def find_tasks(cmd):
    my_query = {}
    for attribute in cmd.__dict__:
        if getattr(cmd, attribute) != None:
            my_query[attribute] = getattr(cmd, attribute)
    print(my_query)
    tasks_set = tasks_collection.find(my_query)
    return tasks_set

if __name__=="__main__":
    # Set the databasse to interact with
    client = MongoClient("localhost", 27017)
    db = client.todolist
    # set the collection we want to read in
    tasks_collection = db.tasks
    # get the inputs arguments from user
    current_objectlist = user_interface.get_command()
    # get all the tasks from the collection
    query = common_types.Writequery(*current_objectlist)
    id = query.send_query()
    print(id)
    # print the tasks
    # display.print_tasks(tasks_set)


