import sqlite3

conn = sqlite3.connect("diabetes.db")

conn.execute("""
CREATE TABLE records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregnancies INTEGER,
    glucose INTEGER,
    bp INTEGER,
    skin INTEGER,
    insulin INTEGER,
    bmi REAL,
    dpf REAL,
    age INTEGER,
    result TEXT
)
""")

conn.commit()
conn.close()

print("✅ Database created successfully")
