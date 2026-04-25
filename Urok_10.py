import sqlite3

# Створення бази та таблиць
conn = sqlite3.connect("v2222.db")
cur = conn.cursor()
'''
cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    teacher_id INTEGER
);
""")

cur.execute("INSERT INTO Students (name, age) VALUES ('Георгій', 14);")
cur.execute("INSERT INTO Students (name, age) VALUES ('Софія', 12);")
cur.execute("INSERT INTO Students (name, age) VALUES ('Марія', 13);")
cur.execute("INSERT INTO Course (course_name, teacher_id) VALUES ('Python', 1);")
cur.execute("INSERT INTO Course (course_name, teacher_id) VALUES ('Photoshop', 2);")


cur.execute("SELECT name, age From Students WHERE age > 12;")
students = cur.fetchall()

for s in students:
    print(s)
'''

cur.execute("SELECT name FROM Students;")
students = cur.fetchall()
cur.execute("SELECT course_name FROM Course;")
course = cur.fetchall()

print("Студенти:", students)
print("Курси:", course)
conn.commit()
conn.close()
