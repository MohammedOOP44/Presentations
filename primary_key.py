import sqlite3


# ─────────────────────────────────────────
#  CONNECTION
# ─────────────────────────────────────────

def create_connection():
    db = sqlite3.connect("school.db")
    cur = db.cursor()
    return db, cur


# ─────────────────────────────────────────
#  CREATE TABLES
# ─────────────────────────────────────────

def create_tables(db, cur):
    # Students table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            name    TEXT    NOT NULL,
            age     INTEGER,
            grade   TEXT
        )
    """)

    # Courses table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id   INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT    NOT NULL,
            credits     INTEGER
        )
    """)

    # Enrollments table (junction table linking students ↔ courses)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id    INTEGER,
            course_id     INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (course_id)  REFERENCES courses(course_id)
        )
    """)

    db.commit()
    print("Tables created successfully.")


# ─────────────────────────────────────────
#  INSERT DATA
# ─────────────────────────────────────────

def add_student(db, cur, name, age, grade):
    cur.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        (name, age, grade)
    )
    db.commit()
    print(f"Student '{name}' added with ID {cur.lastrowid}.")
    return cur.lastrowid


def add_course(db, cur, course_name, credits):
    cur.execute(
        "INSERT INTO courses (course_name, credits) VALUES (?, ?)",
        (course_name, credits)
    )
    db.commit()
    print(f"Course '{course_name}' added with ID {cur.lastrowid}.")
    return cur.lastrowid


def enroll_student(db, cur, student_id, course_id):
    cur.execute(
        "INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )
    db.commit()
    print(f"Student {student_id} enrolled in course {course_id}.")


# ─────────────────────────────────────────
#  READ DATA (SELECT)
# ─────────────────────────────────────────

def get_all_students(cur):
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    print("\n── All Students ──────────────────────")
    print(f"{'ID':<5} {'Name':<12} {'Age':<6} {'Grade'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<12} {row[2]:<6} {row[3]}")


def get_all_courses(cur):
    cur.execute("SELECT * FROM courses")
    rows = cur.fetchall()
    print("\n── All Courses ───────────────────────")
    print(f"{'ID':<5} {'Course Name':<14} {'Credits'}")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<14} {row[2]}")


# ─────────────────────────────────────────
#  JOIN QUERIES
# ─────────────────────────────────────────

def inner_join(cur):
    """
    INNER JOIN — returns only students who ARE enrolled in at least one course.
    Students with no enrollments are excluded.
    """
    cur.execute("""
        SELECT s.name, c.course_name, c.credits
        FROM students s
        INNER JOIN enrollments e ON s.id = e.student_id
        INNER JOIN courses c     ON e.course_id = c.course_id
    """)
    rows = cur.fetchall()
    print("\n── INNER JOIN: Enrolled students ─────")
    print(f"{'Student':<12} {'Course':<14} {'Credits'}")
    print("-" * 35)
    for row in rows:
        print(f"{row[0]:<12} {row[1]:<14} {row[2]}")


def left_join(cur):
    """
    LEFT JOIN — returns ALL students, even those with no enrollments.
    Students with no enrollments will show NULL for course columns.
    """
    cur.execute("""
        SELECT s.name, c.course_name, c.credits
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        LEFT JOIN courses c     ON e.course_id = c.course_id
    """)
    rows = cur.fetchall()
    print("\n── LEFT JOIN: All students + courses ─")
    print(f"{'Student':<12} {'Course':<14} {'Credits'}")
    print("-" * 35)
    for row in rows:
        course  = row[1] if row[1] else "Not enrolled"
        credits = row[2] if row[2] else "—"
        print(f"{row[0]:<12} {course:<14} {credits}")


def find_unenrolled_students(cur):
    """
    LEFT JOIN + WHERE IS NULL — finds students with NO enrollments.
    A common real-world use case.
    """
    cur.execute("""
        SELECT s.name
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        WHERE e.student_id IS NULL
    """)
    rows = cur.fetchall()
    print("\n── Students NOT enrolled in any course")
    if rows:
        for row in rows:
            print(f"  - {row[0]}")
    else:
        print("  All students are enrolled.")


# ─────────────────────────────────────────
#  MAIN — runs everything in order
# ─────────────────────────────────────────

if __name__ == "__main__":
    db, cur = create_connection()

    # 1. Create tables
    create_tables(db, cur)

    # 2. Insert sample students
    ali_id  = add_student(db, cur, "Ali",  20, "A")
    sara_id = add_student(db, cur, "Sara", 22, "B")
    omar_id = add_student(db, cur, "Omar", 21, "A")  # Omar has NO enrollment

    # 3. Insert sample courses
    math_id    = add_course(db, cur, "Math",    3)
    science_id = add_course(db, cur, "Science", 4)

    # 4. Enroll students  (Omar is intentionally left out)
    enroll_student(db, cur, ali_id,  math_id)
    enroll_student(db, cur, ali_id,  science_id)
    enroll_student(db, cur, sara_id, math_id)

    # 5. Read all data
    get_all_students(cur)
    get_all_courses(cur)

    # 6. JOIN queries
    inner_join(cur)
    left_join(cur)
    find_unenrolled_students(cur)

    db.close()