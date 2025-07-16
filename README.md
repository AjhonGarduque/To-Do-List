# To-Do-List-System  
Week 2 - Python Project(late upload, laptop was broken)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Beginner Python project that simulates a simple terminal-based To-Do list system. Users can add tasks, mark them as done, delete them, and view their current and completed tasks. All data is saved persistently using a JSON file so progress is never lost even after quitting.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FEATURES

ADD TASKS  
- Enter a task name (auto lowercased and stripped).  
- Tasks are stored in a "To-Do" list.  
- Input is validated (no empty tasks).  

MARK TASKS AS DONE  
- Choose a task from the To-Do list.  
- Moves the task to the "DoneTask" list.  
- Removes it from the current To-Do list.  

DELETE TASKS  
- Select a task from the To-Do list.  
- Deletes it permanently from the file.  

VIEW TASKS  
- See all tasks currently in your To-Do list.  
- View completed tasks from the DoneTask list.  
- Outputs are printed in a clean, readable format.  

FILE STORAGE  
- Uses `To_Do list.json` to save/load data persistently.  
- Data remains even after the program is closed.  

---

SAMPLE MENU:  
1. See To-Do list  
2. Update a task in To-Do list  
3. Remove a task in To-Do list  
4. Add a task in To-Do list  
5. See done task in To-Do list  
6. Quit  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Concepts Used

- Variables  
- `if` / `elif` / `else`  
- Loops (`while`)  
- Functions & modular structure  
- Dictionaries & JSON  
- File I/O  
- Input validation  
- Global variables  
- Data persistence  
- Clean and readable UI  

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project was built during my second week of learning Python as a beginner-level terminal application.  
It started as a basic add/print loop just like the student management system to learn how to handle persistent file storage and user input in Python but turned into this

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I was kinda just trying to make a small to-do app but I realized that I was already managing data in files and designing a system... planning to do smth bigger to make up for the lost time. 2 weeks is a big gap. I'll keep on updating the other mini projects.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Version 2 - GUI Upgrade (Tkinter)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Late update again — but I rebuilt the same project with a full graphical interface using tkinter. This version takes everything from the terminal version and adds buttons, listboxes, and real-time visual updates. No more typing manually in the console.


NEW FEATURES:

GUI-BASED TASK SYSTEM:
- Replaced terminal input/output with a user interface.
- Built using Python’s tkinter module.
- Clean layout using grid() — no more hacky filler buttons
  
ADD TASK:
- Enter tasks through an input box (Entry widget)
- Auto lowercased and stripped like before
- Tasks instantly show up in the left listbox.

MARK AS DONE:
- Select a task from the To-Do list and click “Update Task.”
- Task gets moved to the Finished list (right side).
- JSON file is updated in real time.

DELETE TASK
- Select from either To-Do or Finished list.
- Deletes the task permanently from the file
- Handles validation if nothing is selected

FILE LOADING:
- On launch, it loads To_Do list.json
- Auto creates file if it doesn't exist
- Persistent data, even after you closing the window

##Concepts Used in GUI Version:
- Tkinter (GUI layout, event handling)
- grid() layout manager
- Listbox widgets (for task display)
- Buttons + Entry input
- File reading/writing with json
- Input validation
- Refreshing widgets dynamically
- Lowercasing + formatting strings
- Better error handling (curselection() edge cases)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Was supposed to upload this on time but i have limited use on my laptop.
I’m starting to see how it actually trains you to build real systems...managing state, files, error-handling, and UIs(GUI?).
I still needed help figuring out curselection() and some spacing stuff, but I learned more from debugging that than from most tutorials.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Next step: maybe convert this into a .exe or try adding features like task search, sorting, or edit task. Still improving, but already feels more like something I can show.
