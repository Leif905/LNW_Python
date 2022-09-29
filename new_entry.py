import psycopg2
import tkinter as Tk

def new_entry():
    root = Tk()
    root.title('LNW - GUI')
    root.geometry("400x400")

    
    # Create Submit Function for DB
    def submit():
        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()

        # Insert a new User into the DB
        c.execute(
            f"INSERT INTO userdata (firstname, lastname, city, street, bdate) VALUES ('{firstname.get()}', '{lastname.get()}', '{city.get()}', '{street.get()}', '{bdate.get()}')"
        )
                

        conn.commit()

        conn.close()

        # Clears the Text Boxes after 
        firstname.delete(0, Tk.END)
        lastname.delete(0, Tk.END)
        city.delete(0, Tk.END)
        street.delete(0, Tk.END)
        bdate.delete(0, Tk.END)

    # Create Query Function
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

        query_label = Tk.Label(root, text=print_records)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()

        conn.close()

    # Create Text Boxes
    firstname = Tk.Entry(root, width=30)
    firstname.grid(row=0, column=1, padx=20)
    lastname = Tk.Entry(root, width=30)
    lastname.grid(row=1, column=1, padx=20)
    city = Tk.Entry(root, width=30)
    city.grid(row=2, column=1, padx=20)
    street = Tk.Entry(root, width=30)
    street.grid(row=3, column=1, padx=20)
    bdate = Tk.Entry(root, width=30)
    bdate.grid(row=4, column=1, padx=20)

    # Create Text Box Labels
    firstname_label = Tk.Label(root, text="Firstname")
    firstname_label.grid(row=0, column=0)
    lastname_label = Tk.Label(root, text="Lastname")
    lastname_label.grid(row=1, column=0)
    city_label = Tk.Label(root, text="City")
    city_label.grid(row=2, column=0)
    street_label = Tk.Label(root, text="Street")
    street_label.grid(row=3, column=0)
    bdate_label = Tk.Label(root, text="Birthdate")
    bdate_label.grid(row=4, column=0)


    # Create submit button
    submit_btn = Tk.Button(root, text="Add Record to DB", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a query button
    query_btn = Tk.Button(root, text="Show Records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=110)


    root.mainloop()