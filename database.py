import sqlite3 as sql
conn = sql.connect('database.db')
c = conn.cursor()
c.execute("CREATE TABLE project (name text, assignedTo text, status text")
c.execute("INSERT INTO project VALUES ('project1','bob','ongoing')")
c.execute("INSERT INTO project VALUES ('project2','alice','completed')")
c.execute("INSERT INTO project VALUES ('project3','tom','submitted')")
c.execute("INSERT INTO project VALUES ('project4','jack','rejected')")
conn.commit()