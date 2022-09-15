import psycopg2
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Listbox')

def query():
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
    print(records)

    # Loop trough Results

    print_records = ''
    for record in records:
        print_records += str(record[1]) + " " + str(record[2]) + "\n"
    
        return(print_records)

    conn.commit()

    conn.close()

langs = (query)