from flask import Flask,redirect, url_for, render_template, request

app = Flask(__name__)

#provided two path options to home page
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#Post and get method implementation
@app.route("/login", methods = ["POST","GET"])
def login():
    #after submitting if http method is post, then redirect to welcome page
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("welcome",name=user))
    #if http method is get then render the login page.
    else:
        return render_template("login.html")


#page for showing python script in html with iteratable variables
@app.route("/py")
def iterate():
    return render_template("iterate.html",content=["sourabh","billu","ani"])


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
