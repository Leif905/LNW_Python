import psycopg2
from tkinter import *

root = Tk()
root.title('Listbox GUI')
root.geometry("400x400")

# Listbox!
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

class UserEntry:
    def __init__(self, id, firstname, lastname, city, street, bdate):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.street = street
        self.bdate = bdate

    def fullname(self): 
        return f'{self.firstname} {self.lastname}'

# Add list of items
my_list = []

def user_entry_obj():
    try:

        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()

        c.execute("SELECT * FROM userdata")
        records = c.fetchall()


        for i in records:
            # myObj = UserEntry(i[0], i[1], i[2], i[3], i[4], i[5])
            # my_list.append(myObj)
            print(i)
            
            
    finally:
        c.close()   

    
user_entry_obj()
           
    
root.mainloop()