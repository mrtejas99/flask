import sqlite3 as sql
conn = sql.connect('database.db')
print("opened successfully")

conn.execute("CREATE TABLE project (name text, assignedTo text, status text)")
conn.execute("INSERT INTO project VALUES ('project1','bob','ongoing')")
conn.execute("INSERT INTO project VALUES ('project2','alice','completed')")
conn.execute("INSERT INTO project VALUES ('project3','tom','submitted')")
conn.execute("INSERT INTO project VALUES ('project4','jack','rejected')")
print("table created and entries added")
conn.commit()
conn.close()