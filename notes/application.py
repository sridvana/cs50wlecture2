from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    headline = "This is a note taking app"
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", headline=headline, notes=notes)

@app.route("/mynotes", methods=["GET", "POST"])
def mynotes():
    if session["mynotes"] == None:
        session["mynotes"] = []
    headline = "This is a note taking app"
    if request.method == "POST":
        mynote = request.form.get("mynote")
        session["mynotes"].append(mynote)

    return render_template("mynotes.html", headline=headline, mynotes=session["mynotes"])