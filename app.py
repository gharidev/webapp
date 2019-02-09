from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html",title='Login')

@app.route("/forgotpassword")
def forgotpassword():
    return render_template("maintenance.html")

@app.route("/signup")
def signup():
    return render_template("maintenance.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html",title='Contact Us')

@app.route("/terms")
def terms():
    return render_template("maintenance.html") 

@app.route("/datapolicy")
def datapolicy():
    return render_template("maintenance.html")

@app.route("/cookiepolicy")
def cookiepolicy():
    return render_template("maintenance.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html",title='About Us')

if (__name__ == "__main__"):
    app.debug=True
    app.run()