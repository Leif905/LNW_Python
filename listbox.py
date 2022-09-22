from tkinter import *
from UserEntryClass import get_user_entries

root = Tk()
root.title('Listbox GUI')
root.geometry("200x200")

# Listbox!
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

# Create a list with the Objects containing the Data from DB   
my_list = get_user_entries()

# Fill the Listbox 
for i in my_list:
    my_listbox.insert(END, i)

my_listbox.select_set(0)

def items_selected():
    # get all selected indices
    my_listbox.curselection()
    print(my_listbox.curselection())




btnGetID = Button(root, text="GetID", command=items_selected)
btnGetID.pack()

root.mainloop()



# # UserEntry Class for Data from DB
# class UserEntry:
#     def __init__(self, id, firstname, lastname, city, street, bdate) -> None:
#         self.id = id
#         self.firstname = firstname
#         self.lastname = lastname
#         self.city = city
#         self.street = street
#         self.bdate = bdate

#     # StringOverride to display Firstname and Lastname in Listbox
#     def __str__(self) -> str: 
#         return f'{self.firstname} {self.lastname}'

#     # __dict__ to assign Keys and Values
#     def __dict__(self):
#         return {"ID": self.id, "Firstname": self.firstname, "Lastname": self.lastname, "City": self.city, "Street": self.street, "Birthdate": self.bdate}


# # Create Object with Data from DB
# def get_user_entries() -> list:
#     try:

#         conn = psycopg2.connect(
#                         host="localhost",
#                         database="lnwgui",
#                         user="postgres",
#                         password="1234",
#                         port="5432" )

#         c = conn.cursor()

#         c.execute("SELECT * FROM userdata")
#         records = c.fetchall()

#         temp_list = []
#         for i in records:
#             myObj = UserEntry(i[0], i[1], i[2], i[3], i[4], i[5])
#             temp_list.append(myObj)
           
#         return temp_list
            
            
#     finally:
#         c.close()




    


# def select():
#     my_label.config(text=my_listbox.get(ANCHOR))
#     my_temp = my_listbox.get(ANCHOR)
#     print(type(my_temp))

# my_button = Button(root, text="Select", command=select)
# my_button.pack(pady=10)

# global my_label
# my_label = Label(root, text='')
# my_label.pack(pady=5)