from flask import Flask,render_template,request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello():
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM project")
    data = cur.fetchall()
    conn.close()
    return render_template("index.html", names=data)

@app.route("/submit", methods=["POST"])
def bye():
    f = request.form
    
    name = f["project"]
    
    #TODO - Insert SQL Select query to fetch name, assignedTo and status
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM project WHERE name=?",(name,))
    d=cur.fetchall()
    database_name = d[0]
    database_assignedto = d[1]
    database_status = d[2]
    
    return render_template("submit.html", formT={"name": database_name, "assignedTo": database_assignedto, "status": database_status})

if __name__=="__main__":
    app.run(debug=True)
