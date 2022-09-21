from tkinter import *
from UserEntryClass import UserEntry

root = Tk()

Firstname = Label(root, text="Firstname")
Firstname.pack()
firstname = Entry(root, width=50)
firstname.pack()
Lastname = Label(root, text="Lastname")
Lastname.pack()
lastname = Entry(root, width=50)
lastname.pack()
City = Label(root, text="City")
City.pack()
city = Entry(root, width=50)
city.pack()
Street = Label(root, text="Street")
Street.pack()
street = Entry(root, width=50)
street.pack()
Bdate = Label(root, text="Birthdate")
Bdate.pack()
bdate = Entry(root, width=50)
bdate.pack()

def myClick():

    newUserEntry = UserEntry('', firstname.get(), lastname.get(), city.get(), street.get(), bdate.get())
    print(newUserEntry.street)

btnNewUserEntry = Button(root, text="New User Entry", command=myClick)
btnNewUserEntry.pack()

def entryCancel():
    pass

btnEntryCancel = Button(root, text="Cancel", command=root.destroy)
btnEntryCancel.pack()

root.mainloop()