from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return("Hello this is a main page <h1>HELLO This is a first heading<h1>")

@app.route("/<name>")
def user(name):
    return f"hello {name}!"

if __name__ == "__main__":
    print("Starting the flask application")
    app.run(debug=True)