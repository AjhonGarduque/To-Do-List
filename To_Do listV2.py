from tkinter import *
import json
import os

# create the window
window =Tk() 
window.geometry("500x500")
window.title("First GUI")  # yeah, I didn’t bother renaming it yet
window.config(background="Gray")

# space between grid rows and columns (no filler buttons used)
window.grid_columnconfigure(1, minsize=0)
window.grid_rowconfigure(3, minsize=20)

# move task from To_Do to DoneTask
def updateTodo():
    global task
    selection = toDoListbox.curselection()
    if not selection:
        return  # don’t crash if nothing’s selected

    updAsk = toDoListbox.get(selection[0]).lower()
    task["DoneTask"].append(updAsk)
    task["To_Do"].remove(updAsk)

    # save to json
    with open("To_Do list.json", "w") as file:
        json.dump(task, file, indent=4)

    # refresh listboxes
    toDoListbox.delete(0, END)
    finishedTaskListbox.delete(0, END)
    loadFile()

# delete selected task from either list
def deleteToDo():
    global task
    finForDel = finishedTaskListbox.curselection()
    todoForDel = toDoListbox.curselection()

    if not finForDel and not todoForDel:
        return  # nothing selected, skip

    # delete from To_Do
    if todoForDel:
        delAsk = toDoListbox.get(todoForDel[0]).lower()
        if delAsk in task["To_Do"]:
            task["To_Do"].remove(delAsk)

    # delete from DoneTask
    if finForDel:
        delAsk = finishedTaskListbox.get(finForDel[0]).lower()
        if delAsk in task["DoneTask"]:
            task["DoneTask"].remove(delAsk)

    # update the file
    with open("To_Do list.json", "w") as file:
        json.dump(task, file, indent=4)

    # refresh both listboxes
    toDoListbox.delete(0, END)
    finishedTaskListbox.delete(0, END)
    loadFile()

# add task from entry box
def addToDo():
    global task
    newTask = addTaskEntry.get().strip().lower()
    if not newTask:
        return  # ignore empty

    if newTask in task["To_Do"]:
        return  # ignore duplicates

    task["To_Do"].append(newTask)

    # save to file
    with open("To_Do list.json", "w") as file:
        json.dump(task, file, indent=4)

    # clear entry and refresh list
    toDoListbox.delete(0, END)
    finishedTaskListbox.delete(0, END)
    addTaskEntry.delete(0, END)
    loadFile()

# load the JSON and show the data in the listboxes
def loadFile():
    global task

    # create the file if it doesn't exist
    if not os.path.exists("To_Do list.json"):
        with open("To_Do list.json", "w") as file:
            json.dump({"To_Do": [], "Done Task": []}, file)

    with open("To_Do list.json", "r") as file:
        task = json.load(file)

    # display tasks in their listboxes
    for item in task.get("To_Do", []):
        toDoListbox.insert(END, item.lower())

    for item in task.get("DoneTask", []):
        finishedTaskListbox.insert(END, item.lower())

# GUI labels and listboxes setup
toDoLabel = Label(window, text="To Do Task", font=("TimesNewRoman", 10))
toDoLabel.grid(row=1, column=0)

toDoListbox = Listbox(window, font=("TimesNewRoman", 10))
toDoListbox.grid(row=2, column=0, padx=10)

finishedTaskLabel = Label(window, text="Finished Task", font=("TimesNewRoman", 10))
finishedTaskLabel.grid(row=1, column=3)

finishedTaskListbox = Listbox(window, font=("TimesNewRoman", 10))
finishedTaskListbox.grid(row=2, column=3)

# button to add task
addTask = Button(window, text="Add Task", command=addToDo, font=("TimesNewRoman", 10))
addTask.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# entry box to type task
addTaskEntry = Entry(window, text="Enter Task", width=30)
addTaskEntry.grid(row=4, column=2)

# button to move task from To_Do to Done
updateTask = Button(window, text="Update Task", command=updateTodo, font=("TimesNewRoman", 10))
updateTask.grid(row=5, column=0, padx=10, pady=5, sticky="w")

# button to delete task from either list
removeTask = Button(window, text="Remove a Task", command=deleteToDo, font=("TimesNewRoman", 10))
removeTask.grid(row=6, column=0, padx=10, pady=5, sticky="w")

# load data and start app
loadFile()
window.mainloop()
