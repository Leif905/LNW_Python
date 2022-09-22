import psycopg2

# UserEntry Class for Data from DB
class UserEntry:
    def __init__(self, id, firstname, lastname, city, street, bdate) -> None:
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.street = street
        self.bdate = bdate

    # StringOverride to display Firstname and Lastname in Listbox
    def __str__(self) -> str: 
        return f'{self.firstname} {self.lastname}'

    # __dict__ to assign Keys and Values
    def __dict__(self):
        return {"ID": self.id, "Firstname": self.firstname, "Lastname": self.lastname, "City": self.city, "Street": self.street, "Birthdate": self.bdate}


# Create Object with Data from DB
def get_user_entries() -> list:
    try:

        conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

        c = conn.cursor()

        c.execute("SELECT * FROM userdata")
        records = c.fetchall()

        temp_list = []
        for i in records:
            myObj = UserEntry(i[0], i[1], i[2], i[3], i[4], i[5])
            temp_list.append(myObj)
            print(type(i))
            
           
        return temp_list
            
            
    finally:
        c.close()

# def damnlistbox():

#     for entry in get_user_entries():
#         print (entry)
