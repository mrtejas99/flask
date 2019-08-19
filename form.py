from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/submit", methods=["POST"])
def bye():
	f = request.form
	return render_template("submit.html", formT=f)

if __name__=="__main__":
    app.run(debug=True)
