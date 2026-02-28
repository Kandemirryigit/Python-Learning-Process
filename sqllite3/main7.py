#############
# DELETE ROWS 
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

cur.execute("DELETE FROM students")

cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",('Ali',20,85.5))
cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",('Ayşe',28,90.0))
cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",('Ali',15,62.6))

cur.execute("""
DELETE FROM students
WHERE age<20
""")

conn.commit()

cur.execute("""
SELECT * FROM students
""")

for row in cur.fetchall():
    print(row)


conn.close()

print("Data Deleted")
