def fill_listbox():
    # Fill the Listbox 
    for myentry in records:
        index_list.append(myentry)
        my_listbox.insert(END, f"{myentry[1]} {myentry[2]}")
        

        

    my_listbox.select_set(0)

    myentry = index_list[my_listbox.curselection()[0]]
    
    entry_id = myentry[0]

    return entry_id