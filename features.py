from flask import Blueprint, render_template

feature = Blueprint("feature", __name__, static_folder='static', template_folder='templates')

#page for showing agian home page but with different route('features/view') in blueprint py script.
@feature.route('/view')
def iterate():
    return render_template("home.html")
