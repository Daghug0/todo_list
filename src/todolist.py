#!usr/bin/python3

from pymongo import MongoClient

class UserCommand:
    def __init__(self, owner, due_date):
        if not owner == "":
            self.owner = owner
        if not due_date == "":
            self.due_date = due_date
        

def get_command_from_user():
    #get owner from keyboard
    owner = input('Type owner (only alpha characters)\n')
    #et duedate from keyboard
    duedate = input('Type due date (format YYYYMMDD)\n')
    cmd = UserCommand(owner, duedate)
    return cmd

#This function find tasks in mongoDB based on user command
# Input     : UserCommand object
# Output    : Cursor of mongoDB documents containing requested tasks
def find_tasks(cmd):
    my_query = {}
    for attribute in cmd.__dict__:
        my_query[attribute] = getattr(cmd, attribute)
    
    tasks_set = tasks_collection.find(my_query)
    return tasks_set

def print_tasks(tasks_set):
    for task in tasks_set:
        print(task)

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
    print_tasks(tasks_set)


