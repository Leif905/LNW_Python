import psycopg2
from tkinter import *



def alterentry(user_id):
    root = Tk()
    root.title('LNW - GUI')
    root.geometry("400x400")

    conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

    c = conn.cursor()

        # Insert a new User into the DB
    c.execute(
            f"SELECT firstname, lastname, city, street, bdate FROM userdata WHERE id={user_id}"
        )
        
    active_user = c.fetchall()
    print(active_user)
        

         
                

    conn.commit()

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
                f"UPDATE userdata SET firstname = '{firstname.get()}', lastname = '{lastname.get()}', city = '{city.get()}', street = '{street.get()}', bdate =  '{bdate.get()}' WHERE id={user_id}"
            )
        
        
        

         
                

        conn.commit()

        conn.close()

        # Clears the Text Boxes after 
        # firstname.insert(0, END)
        # lastname.delete(0, END)
        # city.delete(0, END)
        # street.delete(0, END)
        # bdate.delete(0, END)

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

        query_label = Label(root, text=print_records)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()

        conn.close()

    

    # Create Text Boxes
    firstname = Entry(root, width=30)
    firstname.insert(END, active_user[0][0])
    firstname.grid(row=0, column=1, padx=20)
    lastname = Entry(root, width=30)
    lastname.insert(END, active_user[0][1])
    lastname.grid(row=1, column=1, padx=20)
    city = Entry(root, width=30)
    city.insert(END, active_user[0][2])
    city.grid(row=2, column=1, padx=20)
    street = Entry(root, width=30)
    street.insert(END, active_user[0][3])
    street.grid(row=3, column=1, padx=20)
    bdate = Entry(root, width=30)
    bdate.insert(END, active_user[0][4])
    bdate.grid(row=4, column=1, padx=20)

    # Create Text Box Labels
    firstname_label = Label(root, text="Vorname")
    firstname_label.grid(row=0, column=0)
    lastname_label = Label(root, text="Nachname")
    lastname_label.grid(row=1, column=0)
    city_label = Label(root, text="Stadt")
    city_label.grid(row=2, column=0)
    street_label = Label(root, text="Straße")
    street_label.grid(row=3, column=0)
    bdate_label = Label(root, text="Geburtsdatum")
    bdate_label.grid(row=4, column=0)


    # Create submit button
    submit_btn = Button(root, text="Update Entry", command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a Query Button
    query_btn = Button(root, text="Show Records", command=query)
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=110)


    root.mainloop()