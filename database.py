import sqlite3

def get_db_connection():
    conn = sqlite3.connect('log.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            port TEXT,
            method TEXT,
            path TEXT,
            country TEXT,
            region TEXT,
            city TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()
