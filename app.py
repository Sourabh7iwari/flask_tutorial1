from flask import Flask,redirect, url_for, render_template

app = Flask(__name__)

#provided two path options to home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",content=["sourabh","billu","ani"])

#path with variable
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>HELLO {name}! you're wellcome to this page.<h1>"

#redirecting new user to welcome page
@app.route("/<newuser>")
def newuser(newuser):
    return redirect(url_for("welcome",name="newuser"))

if __name__ == "__main__":
    print("Starting the flask application")
    app.run(debug=True)