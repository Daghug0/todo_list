#!bin/python3

#This file run our application to manage a todolist

from lib import user_interface,database_manager,display

if __name__=="__main__":
    # init the database client
    db_manager = database_manager.DataBaseManager()
    # get the inputs arguments from user
    crud_operation, query_objects = user_interface.get_command()
    # treatment depending on the operation to perform
    match(crud_operation):
        case "write":
            # In case of write, insert a task on DB and read it from the returned ID
            # before reading a task, verify if there is no existing task with the same title
            if db_manager.is_present():
                result_write = db_manager.write(query_objects)
                if result_write.acknowledged:
                    print("write success")
                    result_read = db_manager.read({"_id" : result_write.inserted_id})
                else :
                    print("write failure : Something went wrong")
        case "read":
            # in case of read, read the tasks based on the given criterias
            result_read = db_manager.read(query_objects)
        case "modify":
            # In case of modify:
            # Use the title arguments of the query object to be the filter
            result_read = db_manager.read({"title" : query_objects["title"]})
            query_objects.pop("title")
            if len(result_read) == 0:
                print("modification failure : Your task hasn't been found, try again later...")
                exit()
            # if several, ask for the user to chose 1
            elif len(result_read ) > 1:
                display.print_task_table(result_read)
                choosen_task_index = user_interface.chose_task(len(result_read))
                element_to_modify = result_read[choosen_task_index]
            else :
                element_to_modify = result_read[0]
            # modify the task choosen by the input arguments
            result_modify = db_manager.modify(element_to_modify, query_objects)
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


