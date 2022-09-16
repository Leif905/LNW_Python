import psycopg2
from tkinter import *

root = Tk()
root.title('Listbox GUI')
root.geometry("400x400")

# Listbox!
my_listbox = Listbox(root)
my_listbox.pack(pady=15)

# Create Query Function
def query():
    try:
        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()

        # Query the DB
        c.execute("SELECT * FROM userdata")
        records = c.fetchall()

        # Loop trough Results

        new_list = []
        for record in records:
            new_list.append(str(record[0]) + " " + str(record[1]) + " " + str(record[2]))
        return new_list
        
        # conn.commit()
    finally:
        conn.close()

# Add list of items
my_list = []

# TODO
# id aus query als Position an .insert übergeben!!!

# for x in query():
#     print(x[0])
#     print((x[1:]).lstrip())
    

for x in query():
##    # my_list.append(x)
    my_listbox.insert((x[0]), (x[1:]).lstrip())


# for item in my_list:
#      my_listbox.insert(END, item)
    


root.mainloop()