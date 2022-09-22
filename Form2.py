from turtle import left
import psycopg2
from tkinter import *
from UserEntryClass import UserEntry, get_user_entries

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

    newUserEntry = UserEntry(NONE, firstname.get(), lastname.get(), city.get(), street.get(), bdate.get())
    print(newUserEntry)
    
    
def myClickDB():

    newUserEntry = UserEntry(NONE, firstname.get(), lastname.get(), city.get(), street.get(), bdate.get())
    input = (newUserEntry.firstname, newUserEntry.lastname, newUserEntry.city, newUserEntry.street, newUserEntry.bdate)
    try:

        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()
        c.execute(f'INSERT INTO userdata (firstname, lastname, city, street, bdate) VALUES {input}')
        conn.commit()
            

    finally:
        c.close()
        conn.close()
    

def get_id():

    try:

        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()

        c.execute("SELECT id FROM userdata")
        records = c.fetchall()

        print(records)
            
            
    finally:
        c.close()



btnEntryCancel = Button(root, text="Cancel",command=root.destroy)
btnEntryCancel.pack(side=RIGHT, padx=0, pady=0)

btnNewDBEntry = Button(root, text="New DB Entry", command=myClickDB)
btnNewDBEntry.pack(side=LEFT)

btnGetID = Button(root, text="GetID", command=get_id)
btnGetID.place(x=240, y=180)


root.mainloop()