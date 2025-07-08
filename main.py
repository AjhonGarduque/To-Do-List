import json

task = {}
to_do = []
doneTask = []

def menu():
    global task

    with open("To_Do list.json", "r")as file:
        task = json.load(file)

    if "To_Do" not in task:
        task["To_Do"] = []

    if "DoneTask" not in task:
        task["DoneTask"] = []

    while True:
        print("-" *35)
        print("1.See To-Do list")
        print("2.Update a task in To-Do list")
        print("3.Remove a task in To-Do list")
        print("4.Add a task in To-Do list")
        print("5.See done task in To-Do list")
        print("6.Quit")
        ask = int(input("What do you want to do? "))
        if ask == 1:
            seeAllToDo()
        elif ask == 2:
            updateTodo()
        elif ask == 3:
            deleteToDo()
        elif ask == 4:
            addToDo()
        elif ask == 5:
            seeDoneToDo()
        elif ask == 6:
            break

def seeDoneToDo():
    global task
    print("Done tasks for today:")
    for i in task["DoneTask"]:
        print("-", i.capitalize())

def updateTodo():
    global task
    if "DoneTask" not in task:
        task["DoneTask"] = []

    print("Your tasks for today:")
    for i in task.get("To_Do", []):
        print("-", i.capitalize())

    while True:
        updAsk = str(input("What task is done? ")).strip().lower()
        if updAsk == "q":
            print("Cancelled")
            return
        elif updAsk in task.get("To_Do", []):
            task["DoneTask"].append(updAsk)
            task["To_Do"].remove(updAsk)
            print(f"{updAsk} updated")
        elif updAsk not in task.get("To_Do", []):
            print(f"{updAsk} not in To-Do list")
        elif updAsk == "":
            continue
        
        with open("To_Do list.json", "w") as file:
            json.dump(task, file, indent=4)

def deleteToDo():
    print("Your tasks for today:")
    for i in task["To_Do"]:
        print("-", i.capitalize())

    while True:
        delTask = input("What task do you want to delete? ").strip().lower()
        if delTask == "q":
            return
        elif delTask in task.get("To_Do", []):
            task["To_Do"].remove(delTask)
            print(f"{delTask} is removed")
        elif delTask not in task.get("To_Do", []):
            print(f"{delTask} not in To Do list")
        elif delTask == "":
            continue

        with open("To_Do list.json", "w") as file:
            json.dump(task, file, indent=4)

def addToDo():
    global task
    if "To_Do" not in task:
        task["To_Do"] = []

    while True:
        add = str(input("Enter new Task: ")).strip().lower()
        if add == "q":
            print("Cancelled")
            return
        elif add == "":
            continue
        else:
            task["To_Do"].append(add)
            
        with open("To_Do list.json", "w") as file:
            json.dump(task, file, indent=4)
            print(f"{add} added in to-do list")


def seeAllToDo():
    global task

    print("Your tasks for today:")
    
    for i in task["To_Do"]:
        print("-", i.capitalize())
       



menu()
