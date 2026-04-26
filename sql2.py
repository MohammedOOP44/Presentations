import sqlite3 

con = sqlite3.connect('sq66.db')
cursor = con.cursor()
movies = [
    ('the godfather','crime',1970),
    ('invincible','adventure',2021),
    ('daredevil','sci-fi',2025),
    ('the amazing spider man','action',2012),
    ('fight club','drama',1999),
]

cursor.executemany("INSERT INTO movie VALUES(?,?,?)",movies)

con.commit()
con.close()