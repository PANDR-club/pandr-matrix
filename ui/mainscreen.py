import tkinter as tk
from tkinter import ttk
from utils.bin_dec_hex_tools import randBin, randHex, randDec

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)

notebook = ttk.Notebook(window) # Manages a collection of windows/displays

mainTab = tk.Frame(notebook)
baseNTab = tk.Frame(notebook)

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.pack(expand=True, fill='both') # Expand fills space not otherwise used, fill will fill space on x and y axis

exitBtn = tk.Button(mainTab, text='Exit', command=window.quit, width=20)
exitBtn.pack()

options_list = ["Binary", "Hexadecimal", "Decimal"]
valueofchoice = tk.StringVar(baseNTab)
valueofchoice.set("Select an Option")

question_menu = tk.OptionMenu(baseNTab, valueofchoice, *options_list) 
question_menu.pack()

def print_answers():
    displaychoice = valueofchoice.get()
    if displaychoice == "Binary":
        return questiondisplay.config(text=f"{randBin()} \n{randBin()} \n{randBin()} \n{randBin()} ", font=("Arial", 20))
    elif displaychoice == "Hexadecimal":
        return questiondisplay.config(text=f"{randHex()} \n{randHex()} \n{randHex()} \n{randHex()} ", font=("Arial", 20))
    elif displaychoice == "Decimal":
        return questiondisplay.config(text=f"{randDec()} \n{randDec()} \n{randDec()} \n{randDec()} ", font=("Arial", 20))

submit_button = tk.Button(baseNTab, text='Submit', command=print_answers) 
submit_button.pack()

#Binary Display
questiondisplay = tk.Label(baseNTab)
questiondisplay.pack()

window.mainloop()

