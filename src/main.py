#!bin/python3

#This file run our application to manage a todolist

from api import DataBaseManager
from user_interface import UIManager 
from display import DisplayManager
from utils import OperationType


if __name__=="__main__":
    # init the database client
    disp_manager = DisplayManager()
    # Create the User Interface Manager that asks for operation
    with UIManager() as ui_manager:
        ui_manager = UIManager()
        # Get the operation that have been requested and the arguments associated
        ui_manager.request_all()
        crud_operation = ui_manager.get_operation()
        dict_query = ui_manager.get_arguments_data()
    # treatment depending on the operation to perform
        with DataBaseManager() as db_manager:
            match(crud_operation):
                case OperationType.READ:
                    results = db_manager.read_tasks(dict_query)
                case OperationType.WRITE:
                    results = db_manager.write_task(dict_query)
                case OperationType.MODIFY:
                    #differenciate the filter of the command (the title) from the update arguments
                    task_filter = {"title": dict_query.pop("title")}
                    #count the number of tasks corresponding to the filter
                    task_count = db_manager.count_task(task_filter)
                    # If no task is found, display a message and exit
                    if task_count == 0:
                        print("No task found with these criteria, exiting...")
                        raise SystemExit
                    #else, display the found tasks and ask the user to chose one
                    elif task_count > 1:
                        print("Several tasks have been found corresponding to the title.")
                        tasks_found = db_manager.read_tasks(task_filter)
                        disp_manager.display_tasks(db_manager.read_tasks(tasks_found))
                        ui_manager.request_index()
                        index_to_modify = ui_manager.get_chosen_task_index()
                        task_to_modify = tasks_found[index_to_modify]
                        task_filter = task_to_modify
                    db_manager.modify_task(task_filter,dict_query)

                    
                    results = db_manager.delete_task(dict_query)
            for result in results:
                print(result)
        #         case OperationType.WRITE:
        #             # modify date object so that it reads "before a due date"
        #             if "due_date" in query_objects.keys():
        #                 query_objects["due_date"] = {"$lt" : query_objects["due_date"]}
        #             # in case of read, read the tasks based on the given criterias
        #             result_read = db_manager.read_tasks(query_objects)
        #         case OperationType.DELETE:
        #             # In case of delete:
        #             # Use the title arguments of the query object to be the filter
        #             task_to_delete = find_exact_task({"title" : query_objects["title"]})
        #             if task_to_delete == None:
        #                 print("No task has been found corresponding to your query, exiting...")
        #                 exit()
        #             # Modify the task choosen by the input arguments
        #             result_delete = db_manager.delete(task_to_delete)
        #             if result_delete.acknowledged:
        #                 print("deletion success")
        #             else :
        #                 print("deletion failure : Something went wrong")
        #         case utils.OperationType.MODIFY:
        #             # In case of modify:
        #             # Use the title arguments of the query object to be the filter
        #             task_to_modify = find_exact_task({"title" : query_objects["title"]})
        #             if task_to_modify == None:
        #                 print("No task has been found corresponding to your query, exiting...")
        #                 exit()
        #             # Modify the task choosen with updates arguments
        #             updates = {"$set" : query_objects}
        #             result_modify = db_manager.modify(task_to_modify, updates)
        #             if result_modify.acknowledged:
        #                 print("modification success")
        #                 result_read = db_manager.read_tasks({"_id" : task_to_modify["_id"]})
        #             else :
        #                 print("modification failure : Something went wrong")
        # #print the tasks retrieved except if it was a delete operation
        # if (crud_operation != "delete"):
        #     disp_manager.create_table(result_read)


