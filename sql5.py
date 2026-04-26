# Delete data 

import sqlite3

db = sqlite3.connect('sq66.db') # connect
cur = db.cursor() # edit -> SQL -> cursor
cur.execute("DELETE FROM movie WHERE rowid = 1")
cur.execute("SELECT rowid,* FROM movie")
data = cur.fetchall()
for i in data :
    print(i)


db.commit()
db.close()

