# To Do List Manager

task = []

print('** Your to do list **')
print('Things to do: add, view, delete, complete, exit\n')

while True:
    Things_to_do = input('Enter What you want to do: ').strip().lower()

# Add a task with priority
if Things_to_do == 'add':
   entry = input('Enter task (format: Task description - priority): ').strip()
   if "-" in entry:
       task, priority = entry.split('-', 1) 
       task = task.strip()
       priority = priority.strip()
       tasks.append({"task": task, "priority": priority, "done": False})
   else:
       print("Invalid Entry. Please Enter Task description - priority")

# to view tasks       

elif Things_to_do == "View":
    if not tasks:
        print("No listed task")
    else:
        print("** Your to do list **")
        for i, t in enumerate(tasks, start=1):
            status = "Done" if t["done"] else "Working on it!"
            print(f"{i}. {t['task']} (priority: {t[priority]}) - {status}")
        print()  

# To delete a task

elif Things_to_do == "delete":
    if not tasks:
        print("There are no tasks to delete")
    else:
        try:
            num = int(input("Enter the task number you wish to delete: "))
            if 1<= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Deleted: {removed['task']}")
            else:
                print(" In valid task number.")
        except ValueError:
            print("Try entering a valid task number.")  

# Tasks completed

elif Things_to_do == "complete":
    if not tasks:
        print("No task to complete")
    else:
        try:
            num = int(input("Enter the task number to complete: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print(f"Task completed : {tasks[num -1]['task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid task number.")

# To exit 

elif Things_to_do == "exit":
    print("** Recap **")
    completed = sum(1 for t in tasks if t["done"])
    pending = len(tasks) - completed
    print(f"Tasks Completed :{completed}")
    print(f"Working on it : {pending}")
                                                       

else:
    print("Invalid Entry. Please  select add, view, delete, complete or exit")

    