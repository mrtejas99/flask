<<<<<<< HEAD
from flask import Flask,render_template,request
=======
from flask import Flask,render_template, request
>>>>>>> 4f39ba854efb47acd894807a8f0e1b2d6b9b420a
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
    
    return render_template("submit.html", formT=f)

if __name__=="__main__":
    app.run(debug=True)
