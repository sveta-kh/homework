########################
##The To-Do List Trap##
#######################

#wrong way:
#task_list is mutable, same list is used everytime
#New tasks are added to the same list.

def add_task(task_name, task_list = []):
    task_list.append(task_name)
    return task_list

print(add_task("Monitore network"))
print(add_task("Trableshoot network problems"))
print(add_task("Configure new switch"))

#Correct way:
#If task_list is None, a new empty list is created
#Each new task is added to a new list

def add_task(task_name, task_list = None):
    if task_list is None:
        task_list = []
    task_list.append (task_name)    

    return task_list

print(add_task("Study Python"))
print(add_task("Do homework"))
print(add_task("Write Your own Code"))    



    