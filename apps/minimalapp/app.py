from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/name/<name>", methods=["GET", "POST"])
def show_name(name):
    return "Hello, { name }"
 
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")

@app.route("/contact_complete")
def contact_complete():
    return render_template("contact_complete.html")

