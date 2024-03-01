from flask import render_template
from app import app 



@app.route("/")
def index():
    return render_template("index.html")


from werkzeug.exceptions import NotFound

@app.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    print("error", msg)
    return render_template("errors/404.html", msg=msg)
