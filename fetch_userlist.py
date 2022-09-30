import psycopg2
from config import config


def fetch_list():
    params = config()
    conn = psycopg2.connect(**params)

    c = conn.cursor()    

    # fetches all entries, ordered by ID
    c.execute("SELECT * FROM userdata ORDER BY id")
    records = c.fetchall()
    return records

records = fetch_list()