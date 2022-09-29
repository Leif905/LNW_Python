import psycopg2
import tkinter as tk
from config import config

def connect():
        params = config
        conn = psycopg2.connect(**params)
        c = conn.cursor()
        return c, conn
