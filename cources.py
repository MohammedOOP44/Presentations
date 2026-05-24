import sqlite3

def create_connection():
    db = sqlite3.connect("courcees.db")
    cur = db.cursor()
    return db , cur

def Students_Table(db,cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  age INTEGER,
                  grade TEXT)
                  """)
    db.commit()

def courses_table(db,cur):
    cur.execute(""" CREATE TABLE IF NOT EXISTS courses(
                course_id INTEGER PRIMARY KEY AUTOINCREMENT , 
                course_name TEXT NOT NULL,
                credits INTEGER)
             """)
    db.commit()
    
def relations(db,cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS enrollments(
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER,
                course_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(course_id))
                """)
    db.commit()

def add_student(db,cur,name,age,grade):
    cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",(name,age,grade))
    db.commit()

def add_course(db,cur,name,credit):
    cur.execute("INSERT INTO courses (course_name,credits) VALUES (?,?)",(name,credit))
    db.commit()

def enroll_student(db,cur,s_id,c_id):
    cur.execute("INSERT INTO enrollments (student_id,course_id) VALUES (?,?)",(s_id,c_id))
    db.commit()


# ─────────────────────────────────────────
#  READ DATA (SELECT)
# ─────────────────────────────────────────
def get_all_students(cur):
    cur.execute("SELECT * FROM students")
    for i in cur.fetchall():
        print(i)

def get_all_courses(cur):
    cur.execute("SELECT * FROM courses")
    for i in cur.fetchall():
        print(i)
# ─────────────────────────────────────────
#  JOIN QUERIES
# ─────────────────────────────────────────

def inner_join(cur):
    cur.execute("""
                SELECT s.name , c.course_name , c.credits
                FROM students s 
                INNER JOIN enrollments e ON s.id = e.student_id
                INNER JOIN courses c ON e.course_id = c.course_id                
            """)
    for i in cur.fetchall():
        print(i)

def left_join(cur):
    cur.execute("""
                SELECT s.name , c.course_name , c.credits
                FROM students s 
                INNER JOIN enrollments e ON s.id = e.student_id
                INNER JOIN courses c ON e.course_id = c.course_id                
            """)

def enrolled_student():
    pass


    

    

