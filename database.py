import sqlite3
from datetime import datetime

def get_connection():
    conn = sqlite3.connect("admissions.db", check_same_thread=False)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id TEXT PRIMARY KEY,
        name TEXT, age INTEGER, gender TEXT,
        marks TEXT, qualification TEXT, course TEXT,
        eligibility TEXT, timestamp TEXT
    )''')
    conn.commit()
    conn.close()
