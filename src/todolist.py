#!usr/bin/python3

from pymongo import MongoClient

#constants for display max size of each element
ATTR_DISPLAY = {
    "owner"     : 25,
    "due_date"  : 10,
    "title"     : 60
}
LINE_SIZE = ATTR_DISPLAY["owner"] + ATTR_DISPLAY["due_date"] + ATTR_DISPLAY["title"] + 3


class UserCommand:
    def __init__(self, owner, due_date):
        if not owner == "":
            self.owner = owner
        if not due_date == "":
            self.due_date = due_date
        
#This function allow user to prompt his query
# Input     : None
# Output    : Command object initialized from prompted items
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

#This function prints all documents returned by a mongoDB query
# Input     : Cursor of mongoDB documents
# Output    : None
def print_tasks(tasks_set):
    # print the number of elements found without consuming the cursor
    print(str(len(list(tasks_set.clone()))) + " task(s) have been found corresponding to your query : ")
    print("")
    print("OWNER                    |DUE DATE  |TITLE                                                       |")
    print("-"*LINE_SIZE)
    for task in tasks_set:
        format_task(task)

#This function construct a single entry of the table displayed
def format_task(task):
    for attribute in ATTR_DISPLAY:
        format_attribute(task, attribute)
    print("")

#This function print an attribute on the displayed table with the right format
def format_attribute(task,attribute):
    print(task[attribute] + " "*(ATTR_DISPLAY[attribute] -len(task[attribute])) + "|", end="")

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


