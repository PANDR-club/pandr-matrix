import tkinter as tk
from tkinter import ttk
import atexit

from ui.tabs.mainTab import build_main_tab
from ui.tabs.baseNTab import build_basen_tab
from ui.tabs.classTab import build_class_tab


def exitProg():
    window.quit()

atexit.register(exitProg)

window = tk.Tk()
window.title('Matrix Control Panel')
window.minsize(width=1280, height=800)

notebook = ttk.Notebook(window)

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

# Build tabs (logic moved to other files)
build_main_tab(mainTab, exitProg)
build_basen_tab(baseNTab, window)
build_class_tab(classTab)

window.mainloop()