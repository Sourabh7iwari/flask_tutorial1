from flask import Blueprint, render_template

feature = Blueprint("feature", __name__, static_folder='static', template_folder='templates')

#page for showing python script in html with iteratable variables
@feature.route('/view')
def iterate():
    return render_template("home.html")
