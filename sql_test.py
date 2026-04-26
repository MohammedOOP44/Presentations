import sqlite3


with sqlite3.connect('users.db') as db:
    # Table -> students 
    # create -> execute -> cursor 
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER UNIQUE NOT NULL, name TEXT)")

    # Table -> enrollments -> connect (student WITH course)
    cur.execute("CREATE TABLE IF NOT EXISTS enrollments (student_id INTEGER UNIQUE NOT NULL, course_name TEXT)")

    # add data 
    cur.executemany("INSERT INTO students VALUES (?,?)",[(100,'mohammed'),(101,'ali'),(102,'hussen')])
    cur.executemany("INSERT INTO enrollments VALUES (?,?)",[(100,'SQLITE'),(101,'python')])

    print("\n---INNER JOIN RESUILT---\n")
    cur.execute("""
        SELECT students.name,enrollments.course_name
        FROM students 
        INNER JOIN enrollments ON students.id = enrollments.student_id
    """)
    for i in cur.fetchall():
        print(i)

    print("\n\n---LEFT JOIN---\n")
    cur.execute("""
        SELECT students.name,enrollments.course_name
        FROM students
        LEFT JOIN enrollments ON students.id = enrollments.student_id
    """)
    for i in cur.fetchall():
        print(i)
    db.commit()

    


     