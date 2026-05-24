import sqlite3

def create_connection():
    db = sqlite3.connect('lab.db')
    cur = db.cursor()
    return db , cur 

def create_table(db,cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT ,
                age INTEGER,
                grade text
                )
                """)
    db.commit()

def add_student(db,cur,name,age,grade):
    cur.execute("INSERT INTO students (name,age,grade) VALUES (?,?,?)",(name,age,grade))
    db.commit()

def View_Students(cur):
    cur.execute("SELECT * FROM students")
    for i in cur.fetchall():
        print(i)

def remove_student(db,cur,id_wanted):
    cur.execute("DELETE FROM students WHERE id=(?)",(id_wanted,))
    db.commit()

def update_grades(db,cur,student_id,new_grade):
    cur.execute("UPDATE students SET grade = (?) WHERE id = (?)",(new_grade,student_id))
    db.commit()

def search_by_name(cur,name):
    cur.execute(f"SELECT * FROM students WHERE name like (?)",(f"%{name}%",))
    for row in cur.fetchall():
        print(row)

def search_by_grade(cur,grade):
    cur.execute(f"SELECT * FROM students WHERE grade like (?)",(f"%{grade}%",))
    for row in cur.fetchall():
        print(row)

def inteactive_menu_system(cur,db):
    while True :
        print("""
        1. Add Student                      
        2. View All Students                
        3. Update Student Grade             
        4. Delete Student                   
        5. Search by Name                   
        6. Search by Grade                 
        7. Exit                             
            """)
        choice = int(input("select an option: "))
        
        if choice == 1:
            name = input("enter the student name: ")
            age = input("enter the student age: ")
            grade = input("enter the student grade: ")
            add_student(db,cur,name,age,grade)

        elif choice == 2:
            View_Students(cur)

        elif choice == 3:
            st_id = input("enter the id of the student you want to change his grade")
            new_grade = input("enter the the new grade")
            update_grades(db,cur,st_id,new_grade)

        elif choice == 4:
            student_id = input("enter the id of the student that you want to remove")
            remove_student(db,cur,student_id)

        elif choice == 5:
            name = input("Enter the name to search")
            search_by_name(cur,name)

        elif choice == 6:
            grade = input("Enter the student's garde")
            search_by_grade(cur,grade)
        
        elif choice == 7:
            db.close()
            print("exit...")
            break

        else:
            print("invalid choice please choose in (1-7)")

db,cur = create_connection()
create_table(db,cur)

inteactive_menu_system(cur,db)

    
    



