#!bin/python3

#This file run our application to manage a todolist

from api import database_manager
from userIO import display_manager, user_interface

def find_exact_task(query_filter : dict) -> dict | None:
    # Use the title arguments of the query object to be the filter
    result_read = db_manager.read({"title" : query_filter["title"]})
    query_objects.pop("title")
    if len(list(result_read.clone())) == 0:
        return None
    # if several, ask for the user to chose 1
    elif len(list(result_read.clone())) > 1:
        display_manager.print_task_table(result_read)
        choosen_task_index = user_interface.chose_task(len(list(result_read.clone())))
        return result_read[choosen_task_index]
    else :
        return result_read[0]


if __name__=="__main__":
    # init the database client
    with database_manager.DataBaseManager() as db_manager:
        disp_manager = display_manager.DisplayManager()
        # get the inputs arguments from user
        crud_operation, query_objects = user_interface.get_command()
        # treatment depending on the operation to perform
        match(crud_operation):
            case "write":
                # In case of write, insert a task on DB and read it from the returned ID
                # before reading a task, verify if there is no existing task with the same title
                if db_manager.is_present({"title" : query_objects["title"]}):
                    result_write = db_manager.write(query_objects)
                    if result_write.acknowledged:
                        print("write success")
                        result_read = db_manager.read_tasks({"_id" : result_write.inserted_id})
                    else :
                        print("write failure : Something went wrong")
            case "read":
                # modify date object so that it reads "before a due date"
                if "due_date" in query_objects.keys():
                    query_objects["due_date"] = {"$lt" : query_objects["due_date"]}
                # in case of read, read the tasks based on the given criterias
                result_read = db_manager.read_tasks(query_objects)
            case "modify":
                # In case of modify:
                # Use the title arguments of the query object to be the filter
                task_to_modify = find_exact_task({"title" : query_objects["title"]})
                if task_to_modify == None:
                    print("No task has been found corresponding to your query, exiting...")
                    exit()
                # Modify the task choosen with updates arguments
                updates = {"$set" : query_objects}
                result_modify = db_manager.modify(task_to_modify, updates)
                if result_modify.acknowledged:
                    print("modification success")
                    result_read = db_manager.read_tasks({"_id" : task_to_modify["_id"]})
                else :
                    print("modification failure : Something went wrong")
            case "delete":
                # In case of delete:
                # Use the title arguments of the query object to be the filter
                task_to_delete = find_exact_task({"title" : query_objects["title"]})
                if task_to_delete == None:
                    print("No task has been found corresponding to your query, exiting...")
                    exit()
                # Modify the task choosen by the input arguments
                result_delete = db_manager.delete(task_to_delete)
                if result_delete.acknowledged:
                    print("deletion success")
                else :
                    print("deletion failure : Something went wrong")
        #print the tasks retrieved except if it was a delete operation
        if (crud_operation != "delete"):
            disp_manager.create_table(result_read)


