#!bin/python3

#This file run our application and contains the interface for the user to enter his command

from pymongo import MongoClient
from lib import display,date_translation
import datetime
import string

# TYPES AND CLASS DEFINITION AND/OR MODIFICATION
class UserCommand:
    def __init__(self, owner = None , due_date = None):
        self.due_date = due_date

class Person:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
    def get_string(self):
        return self.first_name + " " + self.family_name
    
#print date in DD/MM/YYYY format :
def get_string(self):
    self.strftime('%d/%m/%Y')

#This function allow user to prompt his query
# Input     : None
# Output    : Command object initialized from prompted items
def get_command_from_user():
    #owner = get_owner_from_user()
    owner = None
    due_date = get_date_from_user()
    cmd = UserCommand(owner, due_date)
    return cmd

def get_owner_from_user():
    string_owner = input('Type owner (only alpha characters)\n')
    if string_owner == "":
        return None
    string_splitted = string_owner.split(None, 1)
    isNameValid = (len(string_splitted) == 2)
    while not isNameValid:
        string_owner = input('Incorrect Name format, Type owner (with a space between firstname and family name)\n')
        if string_owner == "":
            return None
        string_splitted = string_owner.split(None, 1)
        isNameValid = (len(string_splitted) == 2)
    return Person(string_splitted[0],string_splitted[1])

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
    # get the command from user input
    cmd = get_command_from_user()
    # get all the tasks from the collection
    tasks_set = find_tasks(cmd)
    # print the tasks
    display.print_tasks(tasks_set)


