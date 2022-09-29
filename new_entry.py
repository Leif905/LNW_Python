import psycopg2
import tkinter as tk
from config import config

def newentry():
    root = tk.Tk()
    root.title('LNW - GUI')
    root.geometry("400x400")

    
    # Create Submit Function for DB
    def submit():
        params = config
        conn = psycopg2.connect(**params)

        c = conn.cursor()

        # Insert a new User into the DB
        c.execute(
            f"INSERT INTO userdata (firstname, lastname, city, street, bdate) VALUES ('{firstname.get()}', '{lastname.get()}', '{city.get()}', '{street.get()}', '{bdate.get()}')"
        )
                

        conn.commit()

        conn.close()

        # Clears the Text Boxes after 
        firstname.delete(0, tk.END)
        lastname.delete(0, tk.END)
        city.delete(0, tk.END)
        street.delete(0, tk.END)
        bdate.delete(0, tk.END)

    

    # Create Text Boxes
    firstname = tk.Entry(root, width=30)
    firstname.grid(row=0, column=1, padx=20)
    lastname = tk.Entry(root, width=30)
    lastname.grid(row=1, column=1, padx=20)
    city = tk.Entry(root, width=30)
    city.grid(row=2, column=1, padx=20)
    street = tk.Entry(root, width=30)
    street.grid(row=3, column=1, padx=20)
    bdate = tk.Entry(root, width=30)
    bdate.grid(row=4, column=1, padx=20)

    # Create Text Box Labels
    firstname_label = tk.Label(root, text="Firstname")
    firstname_label.grid(row=0, column=0)
    lastname_label = tk.Label(root, text="Lastname")
    lastname_label.grid(row=1, column=0)
    city_label = tk.Label(root, text="City")
    city_label.grid(row=2, column=0)
    street_label = tk.Label(root, text="Street")
    street_label.grid(row=3, column=0)
    bdate_label = tk.Label(root, text="Birthdate")
    bdate_label.grid(row=4, column=0)


    # Create submit button
    submit_btn = tk.Button(root, text="Add Record to DB", command=submit)
    submit_btn.grid(row=6, column=0)

    # Create a Cancel button
    cancel_btn = tk.Button(root, text="Cancel", command=root.destroy)
    cancel_btn.grid(row=7, column=0)


    root.mainloop()