#from ui import matrixTools
from utils.bin_dec_hex_tools import randBin, randDec, randHex
import tkinter as tk
from tkinter import ttk
import os

def exitProg():
#    matrixTools.quitMatrix()
    window.quit()

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)
# window.attributes("-fullscreen", True) # Uncomment this for when running on the Pi

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

announcementVar=tk.StringVar()
def submit():
    announcement=announcementVar.get()
    #("    ANNOUNCEMENT    " + announcement + "    ANNOUNCEMENT    ")

    screenPrev.config(text=announcement)
    announcementVar.set("")


announcementEntry = tk.Entry(mainTab,
                             textvariable = announcementVar,
                             font=('DejaVu Sans',10,'normal'))
subBtn=tk.Button(mainTab,text = 'Submit', command = submit)
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
                    width=20)
exitBtn.place(x=492, y=710)

#----- Hex, Dec, Bin generator
options_list = ["Binary", "Hexadecimal", "Decimal"]
basenchoice = tk.StringVar(baseNTab)
basenchoice.set("Select an Option")

question_menu = tk.OptionMenu(baseNTab, basenchoice, *options_list) 
question_menu.pack()

def print_answers():
    displaychoice = basenchoice.get()
    if displaychoice == "Binary":
        return questiondisplay.config(text=f"{randBin()}", font=("Arial", 20))
    elif displaychoice == "Hexadecimal":
        return questiondisplay.config(text=f"{randHex()}", font=("Arial", 20))
    elif displaychoice == "Decimal":
        return questiondisplay.config(text=f"{randDec()}", font=("Arial", 20))

submit_button = tk.Button(baseNTab, text='Submit', command=print_answers) 
submit_button.pack()
#------

#------ Class editor
name_var = tk.StringVar(classTab)
class_var = tk.StringVar(classTab)
ClassOptions = os.listdir("Classes/")
Classchoice = tk.StringVar(classTab)
Classchoice.set("Choose a Class")
if len(ClassOptions) == 0:
    pass
else:
    for i in range(len(ClassOptions)):
        ClassOptions[i] = ClassOptions[i][:-4]
    ClassMenu = tk.OptionMenu(classTab, Classchoice, *ClassOptions)
    ClassMenu.pack()

    
name_var = tk.StringVar(classTab)
class_var = tk.StringVar(classTab)

def addnametoaclass():
    name = name_var.get()
    chosenclass = Classchoice.get()
    with open(f'Classes//{chosenclass}', 'a') as file:
        file.write(f'{name}\n')

def addnewclass():
    schoolclass = class_var.get()
    newclass = open(f"Classes//{schoolclass}.txt", "x")
    newclass.close()
    ClassOptions = os.listdir("Classes/")
    for i in range(len(ClassOptions)):
        ClassOptions[i] = ClassOptions[i][:-4]
    selected_option = tk.StringVar(value=ClassOptions[0])
    ClassMenu['menu'].delete(0, 'end')
    for option in ClassOptions:
        ClassMenu['menu'].add_command(label=option, command=tk._setit(selected_option, option))

classInput = tk.Entry(classTab, textvariable=class_var)
classInput.pack()
addClass_button = tk.Button(classTab, text='Add Class', command=addnewclass)
addClass_button.pack()
nameInput = tk.Entry(classTab, textvariable=name_var)
nameInput.pack()
addName_button = tk.Button(classTab, text='Add Name', command=addnametoaclass)
addName_button.pack()


questiondisplay = tk.Label(baseNTab)
questiondisplay.pack()

window.mainloop()
