from application import app
from flask import render_template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return "<h1>Hello Earth</h1>"