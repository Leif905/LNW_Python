import psycopg2
conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

c = conn.cursor()

# fetches all KEYS
c.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ='userdata'")
namelist = c.fetchall()

# fetches all entries, ordered by ID
c.execute("SELECT * FROM userdata ORDER BY id")
records = c.fetchall()