from viktors_website import viktors_app
from flask import render_template
@viktors_app.route('/')
@viktors_app.route('/index')
def index():
        return render_template("index.html")
