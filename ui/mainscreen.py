from ui import matrixTools
from utils.bin_dec_hex_tools import randBin, randDec, randHex
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont



def exitProg():
    matrixTools.quitMatrix()
    window.quit()

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

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.pack(expand=True, fill='both')

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

options_list = ["Binary", "Hexadecimal", "Decimal"]
valueofchoice = tk.StringVar(baseNTab)
valueofchoice.set("Select an Option")

monospace = tkFont.Font(family='Monospace', size=36)

question_menu = tk.OptionMenu(baseNTab, valueofchoice, *options_list) 

question_menu.config(height=4, font=(40))
dropdown = window.nametowidget(question_menu.menuname)
dropdown.config(font=monospace)

def print_answers():
    displaychoice = valueofchoice.get()
    if displaychoice == "Binary":
        return questiondisplay.config(text=f"{randBin()}", font=monospace)
    elif displaychoice == "Hexadecimal":
        return questiondisplay.config(text=f"{randHex()}", font=monospace)
    elif displaychoice == "Decimal":
        return questiondisplay.config(text=f"{randDec()}", font=monospace)

submit_button = tk.Button(baseNTab, text='Submit', command=print_answers, font=(40), height=4) 

we = tk.Label(baseNTab)
#Binary Display
questiondisplay = tk.Label(baseNTab)

questiondisplay.grid(column=0,columnspan = 2, sticky = tk.W+tk.E, row=2)
question_menu.grid(column=0, row=1, sticky = tk.W+tk.E)
submit_button.grid(column=1, row=1, sticky = tk.W+tk.E)
baseNTab.grid_columnconfigure((0, 1), weight=1)

window.mainloop()


















#graffiti - Riv
