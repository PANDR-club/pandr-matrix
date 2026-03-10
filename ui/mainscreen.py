#from ui import matrixTools
import tkinter as tk
from tkinter import ttk
import atexit

from ui.tabs.mainTab import buildMainTab
from ui.tabs.baseNTab import buildBaseNTab
from ui.tabs.classTab import buildClassTab


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

# Build tabs
buildMainTab(mainTab, exitProg)
buildBaseNTab(baseNTab, window)
buildClassTab(classTab)

window.mainloop()