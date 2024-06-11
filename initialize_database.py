import sqlite3

def initialize_database():
    conn = sqlite3.connect('crime_monitoring.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        time TEXT NOT NULL,
        description TEXT NOT NULL,
        vehicle_registration TEXT NOT NULL,
        location TEXT NOT NULL,
        status TEXT NOT NULL,
        gender TEXT NOT NULL,
        crime_type TEXT NOT NULL,
        most_wanted TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
