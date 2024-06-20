from flask import Flask,redirect, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return("Hello this is a main page <h1>HELLO This is a first heading<h1>")

@app.route("/welcome/<name>")
def user(name):
    return f"<h1>HELLO {name}! you're wellcome to this page.<h1>"

@app.route("/newuser")
def newuser():
    return redirect(url_for("home"))

if __name__ == "__main__":
    print("Starting the flask application")
    app.run(debug=True)