# update data

import sqlite3

db = sqlite3.connect("sq66.db") # open 
cur = db.cursor() # edit -> SQL -> cursor ->
cur.execute("UPDAtE movie SET title = 'takoo' WHERE rowid = 1 ")
cur.execute("SELECT rowid , * FROM movie")
data = cur.fetchall()
for i in data :
    print(i)


db.commit()
db.close()