import tkinter as tk
from fetch_userlist import records
from new_entry import newentry
from update_entry import update_entry

root = tk.Tk()
root.title('Listbox GUI')
root.geometry("400x400")

my_listbox = tk.Listbox(root)
my_listbox.pack(fill=tk.BOTH)

# Create a list with the Objects containing the Data from DB   
index_list = []
    
# Fill the Listbox with records from fetchuserlist
for myentry in records:
    index_list.append(myentry)
    my_listbox.insert(tk.END, f"{myentry[1]} {myentry[2]}")

    my_listbox.select_set(0)

    myentry = index_list[my_listbox.curselection()[0]]
    entry_id = myentry[0]

# gets entry_id of selected_item to update the db_entry
def selected_item():

    for _ in my_listbox.curselection():
        update_entry((index_list[my_listbox.curselection()[0]])[0])
             
# Button for a new entry
new_entry_btn= tk.Button(root, text="New Entry", command=newentry).pack(side=tk.LEFT)
# Button to update an existing entry
update_entry_btn= tk.Button(root, text="Update Entry", command=selected_item).pack(side=tk.LEFT)

root.mainloop()