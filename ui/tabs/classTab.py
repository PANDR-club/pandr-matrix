import tkinter as tk
import os


def build_class_tab(classTab):

    def reloadClassOptionMenu(classChoice, classMenu, classOptions, class_var):
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

        class_var.set('')

    def addnametoaclass():
        name = name_var.get()
        if name.strip() == "":
            return

        if classChoice.get() == "Choose a Class":
            name_var.set('')
            return

        chosenclass = classChoice.get()

        with open(f'Classes//{chosenclass}.txt', 'a') as file:
            file.write(f'{name}\n')

        name_var.set('')

    def addnewclass():
        schoolclass = class_var.get()
        if schoolclass.strip() == "":
            return

        newclass = open(f"Classes//{schoolclass}.txt", "x")
        newclass.close()

        reloadClassOptionMenu(classChoice, classMenu, classOptions, class_var)

    def deleteclass():
        classToDelete = classChoice.get()
        os.remove(f'Classes//{classToDelete}.txt')

        reloadClassOptionMenu(classChoice, classMenu, classOptions, class_var)

    def displayNames():
        displayStudentNames = classChoice.get()

        with open(f'Classes//{displayStudentNames}.txt') as file:
            namesText = file.read()

        namesDisplay.config(text=f'{namesText}', font=("Arial", 20))

    def deleteNames():
        deletedName = str(name_var.get().capitalize())
        deletedNamesClass = classChoice.get()

        with open(f'Classes//{deletedNamesClass}.txt', 'r+') as file:
            namesText = file.readlines()

            listOfStudents = []

            for i in range(len(namesText)):
                listOfStudents.append(namesText[i].capitalize())

            listOfStudents.remove(f'{deletedName}\n')

            file.seek(0)
            file.truncate(0)

            newListOfStudents = ''.join(listOfStudents)
            file.write(newListOfStudents)

        name_var.set('')

    name_var = tk.StringVar(classTab)
    class_var = tk.StringVar(classTab)

    open("Classes//placeholderClass.txt", "w")

    classOptions = os.listdir("Classes/")
    classChoice = tk.StringVar(classTab)
    classChoice.set("Choose a Class")

    for i in range(len(classOptions)):
        classOptions[i] = classOptions[i][:-4]

    classMenu = tk.OptionMenu(classTab, classChoice, *classOptions)
    classMenu.pack()

    os.remove("Classes//placeholderClass.txt")

    reloadClassOptionMenu(classChoice, classMenu, classOptions, class_var)

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