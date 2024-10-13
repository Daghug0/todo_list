#!bin/python3
# This source file contains a library to display element for our todolist application
from lib import date_translation
import datetime
#constants for display max size of each element
ATTR_DISPLAY = {
    "title"     : 60,
    "due_date"  : 10,
    "owner"     : 25
}

LINE_SIZE = ATTR_DISPLAY["title"] + ATTR_DISPLAY["due_date"] + ATTR_DISPLAY["owner"] + 3

#This function prints all documents returned by a mongoDB query
# Input     : Cursor of mongoDB documents
# Output    : None
def print_tasks(tasks_set):
    # print the number of elements found without consuming the cursor
    print(str(len(list(tasks_set.clone()))) + " task(s) have been found corresponding to your query : ")
    print("")
    print("TITLE                                                       |DUE DATE  |OWNER                    |")
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
    if attribute in task:
        if isinstance(task[attribute], str):
            raw_string = task[attribute]
        elif isinstance(task[attribute], datetime.datetime):
            raw_string = task[attribute].strftime('%d/%m/%Y')
        else:
            raw_string = task[attribute].get_string()
    else: 
        raw_string = ""
    attr_len = len(raw_string)
    print(raw_string + " "*(ATTR_DISPLAY[attribute] - attr_len) + "|", end="")