import tkinter as tk
import tkinter.font as tkFont
from utils.bin_dec_hex_tools import randBin, randDec, randHex


def build_basen_tab(baseNTab, window):

    options_list = ["Binary", "Hexadecimal", "Decimal"]

    basenchoice = tk.StringVar(baseNTab)
    basenchoice.set("Select an Option")

    monospace = tkFont.Font(family='Monospace', size=36)

    question_menu = tk.OptionMenu(baseNTab, basenchoice, *options_list)
    question_menu.config(height=4, font=(40))

    dropdown = window.nametowidget(question_menu.menuname)
    dropdown.config(font=monospace)

    questiondisplay = tk.Label(baseNTab)

    def print_answers():
        displaychoice = basenchoice.get()

        if displaychoice == "Binary":
            return questiondisplay.config(text=f"{randBin()}", font=monospace)

        elif displaychoice == "Hexadecimal":
            return questiondisplay.config(text=f"{randHex()}", font=monospace)

        elif displaychoice == "Decimal":
            return questiondisplay.config(text=f"{randDec()}", font=monospace)

    submit_button = tk.Button(baseNTab, text='Submit', command=print_answers)

    questiondisplay.grid(column=0, columnspan=2, sticky=tk.W+tk.E, row=2)
    question_menu.grid(column=0, row=1, sticky=tk.W+tk.E)
    submit_button.grid(column=1, row=1, sticky=tk.W+tk.E)

    baseNTab.grid_columnconfigure((0, 1), weight=1)