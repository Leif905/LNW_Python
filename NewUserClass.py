import psycopg2
conn = psycopg2.connect(
                        host="localhost",
                        database="lnwgui",
                        user="postgres",
                        password="1234",
                        port="5432" )

c = conn.cursor()

c.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME ='userdata'")
namelist = c.fetchall()
dbdict ={}
mylist = []
for x in namelist:
    mylist.append(str(x))

mylist=([s.strip("('),") for s in mylist])
   
c.execute("SELECT * FROM userdata")
records = c.fetchall()

temp_list = []
for i in records:
    newdbdict = {i[0]: {mylist[1]:i[1], mylist[2]:i[2], mylist[3]:i[3], mylist[4]:i[4], mylist[5]:i[5]}}
    #print(i[0], i[1], i[2], i[3], i[4], i[5])
    dbdict.update(newdbdict)
    #print(newdbdict)
    

# def myprint(dbdict):
#         for k, v in dbdict.items():
#             if isinstance(v, dict):
#                 myprint(v)
#             else:
#                 print("{0} : {1}".format(k, v))


# myprint(dbdict)