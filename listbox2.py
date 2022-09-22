import tkinter as tk
from tkinter import *
from UserEntryClass import get_user_entries

root = tk.Tk()
root.title('Listbox GUI')
root.geometry("200x200")

my_listbox = tk.Listbox(root)
my_listbox.pack()

# Create a list with the Objects containing the Data from DB   
my_list = get_user_entries()

# Fill the Listbox 
for myentry in my_list:
    my_listbox.insert(END, myentry)
    

my_listbox.select_set(0)

# print(damnlistbox())





root.mainloop()