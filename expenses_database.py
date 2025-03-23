import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create the expenses table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    item TEXT,
    amount REAL
)
""")
conn.commit()

def saving_to_database(date, category, item, amount):
    cursor.execute("""
    INSERT INTO expenses (date, category, item, amount)
    VALUES (?, ?, ?, ?)
    """, (date, category, item, amount))
    conn.commit()

def fetch_database():
    cursor.execute("SELECT date, category, item, amount FROM expenses")
    return cursor.fetchall()

def clear_database():
    cursor.execute("DELETE FROM expenses")
    conn.commit()