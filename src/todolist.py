#!usr/bin/python3

from pymongo import MongoClient

class UserCommand:
    def __init__(self, owner, due_date):
        self.owner = owner
        self.due_date = int(due_date)



def get_command_from_user():
    owner = input('Type owner\n')
    duedate = input('Type due date\n')
    cmd = UserCommand("John", 36)
       
def get_tasks():
    tasks_set = tasks_collection.find()
    return tasks_set

def print_tasks(tasks_set):
    for task in tasks_set:
        print(task)

if __name__=="__main__":
    #Set the databasse to interact with
    client = MongoClient("localhost", 27017)
    db = client.todolist
    # set the collection we want to read in
    tasks_collection = db.tasks
    # get all the tasks from the collection
    get_command_from_user()
    tasks_set = get_tasks()
    # print the tasks
    print_tasks(tasks_set)


