####################
# SORT QUERY RESULTS
####################

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
cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",('Ali',35,62.6))

conn.commit()

cur.execute("""
SELECT name,grade
FROM students
ORDER BY grade DESC  
""")

for row in cur.fetchall():
    print(row)


conn.close()

print("Data soreted")