import psycopg2

conn = psycopg2.connect(database="userdata",
                       host="localhost",
                       user="postgres",
                       password="1234",
                       port="5432" )

cursor = conn.cursor()

cursor.execute("SELECT firstname, bdate FROM user_data")

print(cursor.fetchall())

conn.close()