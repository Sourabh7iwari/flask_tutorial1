from flask import Flask,redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from features import feature

#initiating flash app
app = Flask(__name__)
app.register_blueprint(feature, url_prefix= "/feature")

#defining the key for data encryption
app.secret_key="encrypt"

#the database URI for SQLAlchemy to use an SQLite database named users.sqlite3
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
#disabling the modification tracking feature of SQLAlchemy
app.config["SQLALCMEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#creating user model for db
class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self,name, email):
        self.name = name
        self.email = email

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

        found_user = users.query.filter_by(name = user).first()

        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user,"")
            db.session.add(usr)
            db.session.commit()

        flash("You logged in succesfully!","info")
        return redirect(url_for("welcome"))
    
    #if http method is get and user is in session then render welcome page.
    else:
        if "user" in session:
            flash("You are already logged in!")
            return redirect(url_for("welcome"))
        #other wise show login page
        else:
            return render_template("login.html")

#page for showing python script in html with iteratable variables
'''@feature.route('/view')
def iterate():
    return render_template("view.html", values=users.query.all())
'''

#path with variable
@app.route("/user", methods=["POST","GET"])
def welcome():
    email= None
    if "user" in session:
        user = session["user"]

        if request.method=="POST":
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash("Email saved!")
        
        else:
            if "email" in session:
                email = session["email"]
        return render_template("welcome.html",email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


#redirecting new user to welcome page
@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("email", None)
    flash("You have been logout", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    print("Starting the flask application")
    app.run(debug=True)
