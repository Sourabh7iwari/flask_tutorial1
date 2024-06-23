from flask import Flask,redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key="encrypt"
#session variable will be stored for 12 hours only 
app.permanent_session_lifetime=timedelta(hours=12)

#provided two path options to home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#Post and get method implementation
@app.route("/login", methods = ["POST","GET"])
def login():
    #after submitting if http method is post, then redirect to welcome page
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("welcome"))
    
    #if http method is get and user is in session then render welcome page.
    else:
        if "user" in session:
            return redirect(url_for("welcome"))
        #other wise show login page
        return render_template("login.html")


#page for showing python script in html with iteratable variables
@app.route("/py")
def iterate():
    return render_template("iterate.html",content=["sourabh","billu","ani"])


#path with variable
@app.route("/welcome/user")
def welcome():
    if "user" in session:
        user = session["user"]
        return f"<h1>HELLO {user}! you're wellcome to this page.<h1>"
    else:
        return redirect(url_for("login"))

#redirecting new user to welcome page
@app.route("/logout")
def newuser():
    session.pop("user",None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    print("Starting the flask application")
    app.run(debug=True)
