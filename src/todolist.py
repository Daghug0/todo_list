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
            result_write = db_manager.write(current_objects)
            if result_write.acknowledged:
                print("write success")
                result_read = db_manager.read({"_id" : result_write.inserted_id})
            else :
                print("write failure : Something went wrong")
        case "read":
            # in case of read, read the tasks based on the given criterias
            result_read = db_manager.read(current_objects)
    #print the tasks retrieved except if it was a delete operation
    if (crud_operation != "delete"):
        display.print_task_table(result_read)


