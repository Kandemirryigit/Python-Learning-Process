###########################
# CREATE DATABASE AND TABLE
###########################

import sqlite3

# Connect to database (creates file if it doesn't exist)
conn=sqlite3.connect("School.db")

# Cursor for SQL commands
cur=conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            grade REAL)
""")

conn.commit()
conn.close()

print("Database and table created")