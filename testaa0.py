import sqlite3

# فتح اتصال بقاعدة بيانات تجريبية في الذاكرة أو ملف
with sqlite3.connect('school.db') as db:
    cur = db.cursor()
    
    # تفعيل دعم المفاتيح الأجنبية (مهم جداً في SQLite)
    cur.execute("PRAGMA foreign_keys = ON")

    # 1. إنشاء الجداول
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS grades (student_id INTEGER, subject TEXT, score INTEGER)")

    # 2. إضافة بيانات (استخدام executemany الذي تعلمناه!)
    students_data = [(1, 'Ahmed'), (2, 'sara'), (3, 'zaid')]
    grades_data = [(1, 'Math', 90), (2, 'Math', 85)] # تلاحظ أن (زيد) رقمه 3 ليس له درجة هنا
    
    cur.executemany("INSERT OR IGNORE INTO students VALUES (?, ?)", students_data)
    cur.executemany("INSERT OR IGNORE INTO grades VALUES (?, ?, ?)", grades_data)

    print("--- INNER JOIN ---")
    cur.execute("""
        SELECT students.name, grades.subject, grades.score
        FROM students
        INNER JOIN grades ON students.id = grades.student_id
    """)
    
    for row in cur.fetchall():
        print(f"student: {row[0]}, subject: {row[1]}, score: {row[2]}")

    print("\n--- LEFT JOIN  ---")
    cur.execute("""
        SELECT students.name, grades.subject, grades.score
        FROM students
        LEFT JOIN grades ON students.id = grades.student_id
    """)
    
    for row in cur.fetchall():
        print(f"student: {row[0]}, subject: {row[1]}, score: {row[2]}") 

    db.commit()  
