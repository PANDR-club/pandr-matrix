import tkinter as tk

def buildMainTab(mainTab, exitProg):
    announcementVar = tk.StringVar()
    def submit():
        announcement = announcementVar.get()
        screenPrev.config(text=announcement)
        announcementVar.set("")

    announcementEntry = tk.Entry(
        mainTab,
        textvariable=announcementVar,
        font=('DejaVu Sans',20,'normal'),
        width=35
    )

    subBtn = tk.Button(
        mainTab,
        text='Submit',
        command=submit,
        font=(16),
        width=20,
        height=2
    )

    screenPrev = tk.Label(mainTab)

    announcementEntry.pack()
    subBtn.pack()
    screenPrev.pack()

    exitBtn = tk.Button(
        mainTab,
        text='Exit',
        bg="red",
        fg="white",
        activebackground="white",
        activeforeground="red",
        command=exitProg,
        font=(20),
        width=35,
        height=2
    )

    exitBtn.pack(side="bottom")