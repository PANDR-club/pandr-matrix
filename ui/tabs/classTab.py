import tkinter as tk
import os


def buildTab(classTab):
    def menuReload(classChoice, classMenu, classOptions, classVar):
        classChoice.set('Choose a Class')
        classMenu['menu'].delete(0, 'end')

        classOptions = os.listdir("Classes/")
        if len(classOptions) != 0:
            for i in range(len(classOptions)):
                classOptions[i] = classOptions[i][:-4]

        for classOption in classOptions:
            classMenu['menu'].add_command(
                label=classOption,
                command=tk._setit(classChoice, classOption)
            )
        classVar.set('')

    def addName():
        name = nameVar.get()
        if name.strip() == "":
            return

        if classChoice.get() == "Choose a Class":
            nameVar.set('')
            return

        classChoice = classChoice.get()
        with open(f'Classes//{classChoice}.txt', 'a') as file:
            file.write(f'{name}\n')

        nameVar.set('')

    def addClass():
        addedClass = classVar.get()
        if addedClass.strip() == "":
            return

        newclass = open(f"Classes//{addedClass}.txt", "x")
        newclass.close()

        menuReload(classChoice, classMenu, classOptions, classVar)

    def deleteClass():
        deletedClass = classChoice.get()
        os.remove(f'Classes//{deletedClass}.txt')

        menuReload(classChoice, classMenu, classOptions, classVar)

    def displayNames():
        displayClass = classChoice.get()

        with open(f'Classes//{displayClass}.txt') as file:
            namesText = file.read()

        namesDisplay.config(text=f'{namesText}', font=("Arial", 20))

    def deleteNames():
        deletedName = str(nameVar.get().capitalize())
        nameLocation = classChoice.get()

        with open(f'Classes//{nameLocation}.txt', 'r+') as file:
            namesText = file.readlines()

            studentList = []

            for i in range(len(namesText)):
                studentList.append(namesText[i].capitalize())

            studentList.remove(f'{deletedName}\n')

            file.seek(0)
            file.truncate(0)

            newStudentList = ''.join(studentList)
            file.write(newStudentList)

        nameVar.set('')

    nameVar = tk.StringVar(classTab)
    classVar = tk.StringVar(classTab)

    open("Classes//placeholderClass.txt", "w")

    classOptions = os.listdir("Classes/")
    classChoice = tk.StringVar(classTab)
    classChoice.set("Choose a Class")

    for i in range(len(classOptions)):
        classOptions[i] = classOptions[i][:-4]

    classMenu = tk.OptionMenu(classTab, classChoice, *classOptions)
    classMenu.pack()

    os.remove("Classes//placeholderClass.txt")

    menuReload(classChoice, classMenu, classOptions, classVar)

    classInput = tk.Entry(classTab, textvariable=classVar)
    classInput.pack()

    addClass_button = tk.Button(classTab, text='Add Class', command=addClass)
    addClass_button.pack()

    deleteClass_button = tk.Button(classTab, text='Delete Class', command=deleteClass)
    deleteClass_button.pack()

    nameInput = tk.Entry(classTab, textvariable=nameVar)
    nameInput.pack()

    addName_button = tk.Button(classTab, text='Add Name', command=addName)
    addName_button.pack()

    deleteName_button = tk.Button(classTab, text='Delete Name', command=deleteNames)
    deleteName_button.pack()

    displayNames_button = tk.Button(classTab, text='Display Names', command=displayNames)
    displayNames_button.pack()

    namesDisplay = tk.Label(classTab)
    namesDisplay.pack()
