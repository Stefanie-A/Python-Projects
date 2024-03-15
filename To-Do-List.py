Tasks = []

def add_task(task):
    Tasks.append(task)

def remove_task(task):
    if task in Tasks:
        Tasks.remove(task)
    else: 
        return "Task not found", 401
    
def view_tasks():
    for i, task in enumerate(Tasks, start=1):
        print("{} {}".format(i, task))


while True:
    print("/nOptions:")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. List Tasks")
    print("4. Quit")

    choice = int(input("Enter your option: "))

    if choice == 1:
       task = input("Enter your task: ")
       Tasks.append(add_task(task))
    elif choice == 2:
        task = input("Enter task to be removed: ")
        remove_task(task)
    elif choice == 3:
        view_tasks()
    elif choice == 4:
        break
    else:
        print("Invalid choice, pls try again.")
    