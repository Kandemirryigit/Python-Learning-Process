#############
# INSERT DATA
#############

import sqlite3

conn=sqlite3.connect("school.db")
cur=conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            grade REAL)
""")


cur.execute("INSERT INTO students VALUES(1,'Ali',20,85.5)")
cur.execute("INSERT INTO students VALUES(2,'Ayşe',21,90.0)")
cur.execute("INSERT INTO students VALUES(3,'Mehmet',19,72.0)")

conn.commit()
conn.close()

print("Data Inserted")