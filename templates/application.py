import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, World! (variable)"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye! (variable)"
    return render_template("index.html", headline=headline)   

@app.route("/checknewyear")
def isitanewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    #new_year = True
    return render_template("newyear.html", new_year=new_year)   

@app.route("/names")
def names():
    headline = "Hello, World! (variable)"
    names = ["Alice", "Brian", "David"]
    return render_template("index.html", names=names, headline=headline)

@app.route("/start")
def start():
    headline = "This is a start page"
    paragraph = "This is a paragraph supposed a bit longer but for now it is very short"
    return render_template("start.html", headline=headline, paragraph=paragraph)

@app.route("/next")
def next():
    headline = "This is a next page"
    paragraph = "This is a paragraph in the next page supposed a bit longer but for now it is very short"
    return render_template("next.html", headline=headline, paragraph=paragraph)