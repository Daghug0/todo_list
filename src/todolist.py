#!bin/python3

#This file run our application and contains the interface for the user to enter his command

from pymongo import MongoClient
from lib import display,date_translation,user_interface
import datetime
import string

def get_date_from_user():
    string_due_date = input('Type due date (format DD/MM/YYYY)\n')
    if (string_due_date) == "":
        return None
    else:
        isDateValid,due_date = date_translation.parse_date_from_string(string_due_date)
    while (not isDateValid):
        string_due_date = input('Incorrect date format, Type due date (format DD/MM/YYYY)\n')
        if (string_due_date) == "":
            return None
        else :
            isDateValid,due_date = date_translation.parse_date_from_string(string_due_date)
    return due_date

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
    # Ask the user for the operation {READ; WRITE; MODIFY; DELETE}
    current_operation = user_interface.get_command()
    # get the command from user input
    cmd = user_interface.get_command()
    # get all the tasks from the collection
    tasks_set = find_tasks(cmd)
    # print the tasks
    display.print_tasks(tasks_set)


