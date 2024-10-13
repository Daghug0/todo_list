Database : Mongo Database
Language : Python3

The aim is to create a CRUD application TODO list.

V1 :
Be able to read tasks from database

V2 : 
Be able to read tasks based on owner of the task and due date

V3 : 
Be able to write a task

V4 :
Be able to add a date to a task or directly attribute it at writing

V5 : 
Be able to add users

V6 :
Be able to attribute a task to a user (existing) (at creation or afterward)

V7 :
Add the state to a task : TO BE DONE ; TO BE REVIEWED ; DONE
By default, a state is set to TO BE DONE when a task is created

V8 :
Add authentication/identification process

V9 :
Define roles : 
ADMIN > Can delete add and delete users
MANAGER > 
- Can add & remove tasks
- Attribute tasks to workers
- Change the due date of a tasks
WORKER > Can change the state of a task

V10 : 
Define a workflow of a task 
The state of a task have to follow the workflow :
TO BE DONE > TO BE REVIEWED > DONE
WORKER can change from STATE 1 to 2
MANAGER can change it from STATE 2 to 3
ADMIN can change the state as he wants

BASIC USER:
    Show the tasks they have to do
    ask for updates
MANAGER:
    1. Ask for operation : Read/write/modify/delete.
    2.In case of read :   
            a.Read criterias : owner and or due 
    3.In case of write :
            a. ask for title (mandatory), due date and owner (optionnal)
    4.In case of modify:
            a. ask for the task to be modified (ID)
            b. ask for the parameter to be modified
            c. ask for the modified parameter
    5.In case of delete:
            a. ask for the ID of the task to be deleted 