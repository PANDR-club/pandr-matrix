import tkinter as tk
from tkinter import ttk
from utils.bin_dec_hex_tools import randBin, randHex, randDec
import subprocess, signal


def runSubprocess(args):
    global matrixProc

    matrixProc = subprocess.Popen(args)

def exitProg():
    global matrixProc

    window.quit()

    if matrixProc:
        matrixProc.send_signal(signal.SIGINT) # This is extremely poor practice, and should be fixed

matrixProc = None

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

notebook.add(mainTab, text='Home')
notebook.add(baseNTab, text='BaseN')
notebook.pack(expand=True, fill='both')

announcementVar=tk.StringVar()
def submit():
    global matrixProc

    announcement=announcementVar.get()
    #("    ANNOUNCEMENT    " + announcement + "    ANNOUNCEMENT    ")

    screenPrev.config(text=announcement)
    announcementVar.set("")

    if matrixProc:
        matrixProc.send_signal(signal.SIGINT) # This is extremely poor practice, and should be fixed

    runSubprocess(['sudo', 'python', '-m', 'matrix.utils.dispText', '-t', announcement, '-x', str(64-len(announcement)*5), '-y', str(32+6)])

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

options_list = ["Binary", "Hexadecimal", "Decimal"]
valueofchoice = tk.StringVar(baseNTab)
valueofchoice.set("Select an Option")

question_menu = tk.OptionMenu(baseNTab, valueofchoice, *options_list) 
question_menu.pack()

def print_answers():
    displaychoice = valueofchoice.get()
    if displaychoice == "Binary":
        return questiondisplay.config(text=f"{randBin()}", font=("Arial", 20))
    elif displaychoice == "Hexadecimal":
        return questiondisplay.config(text=f"{randHex()}", font=("Arial", 20))
    elif displaychoice == "Decimal":
        return questiondisplay.config(text=f"{randDec()}", font=("Arial", 20))

submit_button = tk.Button(baseNTab, text='Submit', command=print_answers) 
submit_button.pack()

#Binary Display
questiondisplay = tk.Label(baseNTab)
questiondisplay.pack()

window.mainloop()
