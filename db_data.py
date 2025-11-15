import sqlite3

conn = sqlite3.connect("revenue.db")
cur = conn.cursor()

for row in cur.execute("SELECT * FROM quarterly_revenue LIMIT 20"):
    print(row)

