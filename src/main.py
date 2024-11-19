#!bin/python3

#This file run our application to manage a todolist

from api.database_manager import DataBaseManager
from user_interface.UI_manager import UIManager 
from display.display_manager import DisplayManager
from utils import utils


if __name__=="__main__":
    # init the database client
    disp_manager = DisplayManager()
    # Create the User Interface Manager that asks for operation
    with UIManager() as ui_manager:
        ui_manager = UIManager()
        # Get the operation that have been requested and the arguments associated
        ui_manager.request_all()
        crud_operation = ui_manager.get_operation()
        arguments = ui_manager.get_arguments()
    # # treatment depending on the operation to perform
    #     with DataBaseManager() as db_manager:
    #         match(crud_operation):
    #             case utils.OperationType.READ:
    #                 DataBaseManager.read(argument_list)
    #             case utils.OperationType.WRITE:
    #                 DataBaseManager.write(argument_list)
    #                 # In case of write, insert a task on DB and read it from the returned ID
    #                 # before reading a task, verify if there is no existing task with the same title
    #                 if db_manager.is_present({"title" : query_objects["title"]}):
    #                     result_write = db_manager.write(query_objects)
    #                     if result_write.acknowledged:
    #                         print("write success")
    #                         result_read = db_manager.read_tasks({"_id" : result_write.inserted_id})
    #                     else :
    #                         print("write failure : Something went wrong")
    #             case utils.OperationType.WRITE:
    #                 # modify date object so that it reads "before a due date"
    #                 if "due_date" in query_objects.keys():
    #                     query_objects["due_date"] = {"$lt" : query_objects["due_date"]}
    #                 # in case of read, read the tasks based on the given criterias
    #                 result_read = db_manager.read_tasks(query_objects)
    #             case utils.OperationType.DELETE:
    #                 # In case of delete:
    #                 # Use the title arguments of the query object to be the filter
    #                 task_to_delete = find_exact_task({"title" : query_objects["title"]})
    #                 if task_to_delete == None:
    #                     print("No task has been found corresponding to your query, exiting...")
    #                     exit()
    #                 # Modify the task choosen by the input arguments
    #                 result_delete = db_manager.delete(task_to_delete)
    #                 if result_delete.acknowledged:
    #                     print("deletion success")
    #                 else :
    #                     print("deletion failure : Something went wrong")
    #             case utils.OperationType.MODIFY:
    #                 # In case of modify:
    #                 # Use the title arguments of the query object to be the filter
    #                 task_to_modify = find_exact_task({"title" : query_objects["title"]})
    #                 if task_to_modify == None:
    #                     print("No task has been found corresponding to your query, exiting...")
    #                     exit()
    #                 # Modify the task choosen with updates arguments
    #                 updates = {"$set" : query_objects}
    #                 result_modify = db_manager.modify(task_to_modify, updates)
    #                 if result_modify.acknowledged:
    #                     print("modification success")
    #                     result_read = db_manager.read_tasks({"_id" : task_to_modify["_id"]})
    #                 else :
    #                     print("modification failure : Something went wrong")
    #     #print the tasks retrieved except if it was a delete operation
    #     if (crud_operation != "delete"):
    #         disp_manager.create_table(result_read)


