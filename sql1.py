import sqlite3

con = sqlite3.connect("sq66.db")

cursor = con.cursor()
cursor.execute("CREATE TABLE movie(title TEXT,Genre TEXT,year INTEGER)")

con.commit()
con.close()