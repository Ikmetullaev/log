import sqlite3
from config import DB_FILENAME

def get_db_connection():
    return sqlite3.connect(DB_FILENAME)

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            port TEXT,
            method TEXT,
            path TEXT,
            country TEXT,
            region TEXT,
            city TEXT,
            loc TEXT,
            timezone TEXT,
            org TEXT,
            postal TEXT,
            device TEXT,
            browser TEXT,
            os TEXT,
            lang TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()
