import sqlite3

# ─────────────────────────────────────────────
# 1. DATABASE CREATION & CONNECTION
# ─────────────────────────────────────────────
def connect():
    db = sqlite3.connect("memory.db")
    cur = db.cursor()
    return cur , db

# ─────────────────────────────────────────────
# 2. TABLE SETUP
# ─────────────────────────────────────────────
def create_table(cur):
    cur.execute(""" 
        CREATE TABLE IF NOT EXISTS students (
                id    INTEGER PRIMARY KEY AUTOINCREMENT ,
                name  TEXT NOT NULL,
                age   INTEGER,
                grade TEXT   
    )
    """)


# ─────────────────────────────────────────────
# 3. CRUD OPERATIONS
# ─────────────────────────────────────────────

def add_student(db,cur):
    name = input("Enter the student name").strip()
    age = input("Enter the student age").strip()
    grade = input("Enter the student grade").strip()

    cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",(name,int(age),grade))

    db.commit()
    print("✅ Student added successfully!\n") 

def view_students(cur):
    
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)


def update_student(db,cur):

    student_id = input("Enter student id to update the grade").strip()
    new_grade = input("Enter new garde").strip()
    
    cur.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade,student_id))
    db.commit()

def delete_student(db,cur):
    student_id = input("enter the student id to delete")

    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))

    db.commit()



    