#from ui import matrixTools
from utils.bin_dec_hex_tools import randBin, randDec, randHex
import tkinter as tk
from tkinter import ttk
import os
import tkinter.font as tkFont
import atexit


def exitProg():
#    matrixTools.quitMatrix()
    window.quit()

atexit.register(exitProg)

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)
#window.attributes("-fullscreen", True) # Uncomment this for when running on the Pi

notebook = ttk.Notebook(window) # Manages a collection of windows/displays

style = ttk.Style()
style.theme_use('default')

style.configure("TNotebook.Tab", padding=[10, 20])

mainTab = tk.Frame(notebook)
baseNTab = tk.Frame(notebook)
classTab = tk.Frame(notebook)

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.add(classTab, text='Class')
notebook.pack(expand=True, fill='both')

# matrixTools.dispClock() # For now just display the clock

announcementVar=tk.StringVar()
def submit():
    announcement=announcementVar.get()
    #("    ANNOUNCEMENT    " + announcement + "    ANNOUNCEMENT    ")

    screenPrev.config(text=announcement)
    announcementVar.set("")

announcementEntry = tk.Entry(mainTab,
                             textvariable = announcementVar,
                             font=('DejaVu Sans',20,'normal'),
                             width=35,)
subBtn=tk.Button(mainTab,
                 text = 'Submit',
                 command = submit,
                 font=(16),
                 width=20,
                 height=2)
screenPrev = tk.Label(mainTab)

announcementEntry.pack()
subBtn.pack()
screenPrev.pack()

notebook.pack(expand=True, fill='both') # Expand fills space not otherwise used, fill will fill space on x and y axis

exitBtn = tk.Button(mainTab,
                    text='Exit',
                    bg="red",
                    fg="white",
                    activebackground="white",
                    activeforeground="red",
                    command=exitProg,
                    font=(20),
                    width=35,
                    height=2)
exitBtn.pack(side="bottom")

#----- Hex, Dec, Bin generator
options_list = ["Binary", "Hexadecimal", "Decimal"]
basenchoice = tk.StringVar(baseNTab)
basenchoice.set("Select an Option")

monospace = tkFont.Font(family='Monospace', size=36)
question_menu = tk.OptionMenu(baseNTab, basenchoice, *options_list)

question_menu.config(height=4, font=(40))
dropdown = window.nametowidget(question_menu.menuname)
dropdown.config(font=monospace)

def print_answers():
    displaychoice = basenchoice.get()
    if displaychoice == "Binary":
        return questiondisplay.config(text=f"{randBin()}", font=monospace)
    elif displaychoice == "Hexadecimal":
        return questiondisplay.config(text=f"{randHex()}", font=monospace)
    elif displaychoice == "Decimal":
        return questiondisplay.config(text=f"{randDec()}", font=monospace)

submit_button = tk.Button(baseNTab, text='Submit', command=print_answers) 
# submit_button.pack()
#------

#------ Class editor
name_var = tk.StringVar(classTab)
class_var = tk.StringVar(classTab)
classOptions = os.listdir("Classes/")
# if len(classOptions) == 0:
#     open("placeholderClass.txt", "w")
classChoice = tk.StringVar(classTab)
classChoice.set("Choose a Class")
if len(classOptions) != 0:
    for i in range(len(classOptions)):
        classOptions[i] = classOptions[i][:-4]
    classMenu = tk.OptionMenu(classTab, classChoice, *classOptions)
    classMenu.pack()
    
name_var = tk.StringVar(classTab)
class_var = tk.StringVar(classTab)

def addnametoaclass():
    name = name_var.get()
    # if name == "":
    #     return
    chosenclass = classChoice.get()
    with open(f'Classes//{chosenclass}.txt', 'a') as file:
        file.write(f'{name}\n')
    name_var.set('')

def addnewclass():
    schoolclass = class_var.get()
    newclass = open(f"Classes//{schoolclass}.txt", "x")
    newclass.close()

    classChoice.set('Choose a Class')
    classMenu['menu'].delete(0, 'end')
    classOptions = os.listdir("Classes/")
    if len(classOptions) != 0:
        for i in range(len(classOptions)):
            classOptions[i] = classOptions[i][:-4]

    for classOption in classOptions:
        classMenu['menu'].add_command(label=classOption, command=tk._setit(classChoice, classOption))
    class_var.set('')

def deleteclass():
    classToDelete = classChoice.get()
    os.remove(f'Classes//{classToDelete}' + '.txt')

    classChoice.set('Choose a Class')
    classMenu['menu'].delete(0, 'end')
    classOptions = os.listdir("Classes/")
    if len(classOptions) != 0:
        for i in range(len(classOptions)):
            classOptions[i] = classOptions[i][:-4]

    for classOption in classOptions:
        classMenu['menu'].add_command(label=classOption, command=tk._setit(classChoice, classOption))

def displayNames():
    displayStudentNames = classChoice.get()
    with open(f'Classes//{displayStudentNames}' + '.txt') as file:
        namesText = file.read()
        namesDisplay.config(text=f'{namesText}', font=("Arial", 20))

def deleteNames():
    deletedName = str(name_var.get().lower())
    deletedNamesClass = classChoice.get()
    with open(f'Classes//{deletedNamesClass}' + '.txt', 'r+') as file:
        namesText = file.readlines()
        listOfStudents = []
        for i in range(len(namesText)):
            listOfStudents.append(namesText[i].lower())
        listOfStudents.remove(f'{deletedName}' + '\n')
        file.seek(0) # Moves pointer to start of file.
        file.truncate(0)
        newListOfStudents = ''.join(listOfStudents)
        file.write(newListOfStudents) 



classInput = tk.Entry(classTab, textvariable=class_var)
classInput.pack()
addClass_button = tk.Button(classTab, text='Add Class', command=addnewclass)
addClass_button.pack()
deleteClass_button = tk.Button(classTab, text='Delete Class', command=deleteclass)
deleteClass_button.pack()
nameInput = tk.Entry(classTab, textvariable=name_var)
nameInput.pack()
addName_button = tk.Button(classTab, text='Add Name', command=addnametoaclass)
addName_button.pack()
deleteName_button = tk.Button(classTab, text='Delete Name', command=deleteNames)
deleteName_button.pack()
displayNames_button = tk.Button(classTab, text='Display Names', command=displayNames)
displayNames_button.pack()
namesDisplay = tk.Label(classTab)
namesDisplay.pack()
#------------------
#Fix bug - Nothing in 'Class Menu Folder' error when adding new class with no existing classes
#Add error checking e.g empty box

questiondisplay = tk.Label(baseNTab)
questiondisplay.grid(column=0,columnspan = 2, sticky = tk.W+tk.E, row=2)
question_menu.grid(column=0, row=1, sticky = tk.W+tk.E)
submit_button.grid(column=1, row=1, sticky = tk.W+tk.E)
baseNTab.grid_columnconfigure((0, 1), weight=1)

window.mainloop()


















#graffiti - Riv
