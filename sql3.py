# read data from the table

import sqlite3

db = sqlite3.connect('sq66.db')
cur = db.cursor()

cur.execute("SELECT rowid,* from movie WHERE rowid BETWEEN 1 AND 5 ")
data = cur.fetchall()
for i in data:
    print(i)

db.commit()
db.close()