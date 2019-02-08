from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("maintenance.html")

@app.route("/signup")
def signup():
    return render_template("maintenance.html")


@app.route("/terms")
def terms():
    return render_template("maintenance.html") 

@app.route("/datapolicy")
def datapolicy():
    return render_template("maintenance.html")

@app.route("/cookiepolicy")
def cookiepolicy():
    return render_template("maintenance.html")

if (__name__ == "__main__"):
    app.run(debug=True)