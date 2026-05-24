import sqlite3

db = sqlite3.connect("memory.db")
cur = db.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.executescript("""
    CREATE TABLE users (
        id    INTEGER PRIMARY KEY AUTOINCREMENT,
        name  TEXT NOT NULL
    );

    CREATE TABLE orders (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id  INTEGER NOT NULL,
        product  TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    );
""")



# Insert data
cur.execute("INSERT INTO users (name) VALUES (?)",('mohammed',))
cur.execute("INSERT INTO orders (user_id,product) VALUES (?,?)",(1,'labtop'))
db.commit()


cur.execute("SELECT * FROM orders")
# Orders for user 1 are now gone
for row in cur.fetchall():
    print(row)

