#!bin/python3

#This file run our application to manage a todolist

from lib import user_interface,database_manager,display

if __name__=="__main__":
    # init the database client
    db_manager = database_manager.DataBaseManager()
    # get the inputs arguments from user
    crud_operation, current_objects = user_interface.get_command()
    # treatment depending on the operation to perform
    match(crud_operation):
        case "write":
            # in case of write, insert a task on DB and read it from the returned ID
            # before reading a task, verify if there is no existing task with the same title
            if db_manager.is_present():
                result_write = db_manager.write(current_objects)
                if result_write.acknowledged:
                    print("write success")
                    result_read = db_manager.read({"_id" : result_write.inserted_id})
                else :
                    print("write failure : Something went wrong")
        case "read":
            # in case of read, read the tasks based on the given criterias
            result_read = db_manager.read(current_objects)
        case "modify":
            # in case of modify, insert a task on DB and read it from the returned ID
            result_modify = db_manager.modify(current_objects)
            if result_modify.acknowledged:
                print("modification success")
                result_read = db_manager.read({"_id" : result_modify.inserted_id})
            else :
                print("modification failure : Something went wrong")
        case "delete":
            #in case of delete, try to read the task with the corresponding filter,
            #then, prompt user if he wants to delete it, or try another.
            if db_manager.delete().acknowledged:
                print("delete success")
            else :
                print ("delete failure, Something went wrong")
    #print the tasks retrieved except if it was a delete operation
    if (crud_operation != "delete"):
        display.print_task_table(result_read)


