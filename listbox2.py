import tkinter as tk
from tkinter import *
import tkinter
from NewUserClass import records
from guifile import entrymask


root = tk.Tk()
root.title('Listbox GUI')
root.geometry("400x400")

my_listbox = tk.Listbox(root)
my_listbox.pack(fill=tk.BOTH)

# Create a list with the Objects containing the Data from DB   


index_list = []
    
# Fill the Listbox 
for myentry in records:
    index_list.append(myentry)
    my_listbox.insert(END, f"{myentry[1]} {myentry[2]}")

    my_listbox.select_set(0)

    myentry = index_list[my_listbox.curselection()[0]]
    entry_id = myentry[0]


new_entry_btn= Button(root, text="Neuer Eintrag", command=entrymask).pack(side=tkinter.LEFT)
alter_entry_btn= Button(root, text="Eintrag bearbeiten", command=entrymask).pack(side=tkinter.LEFT)
root.mainloop()