from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/maria")
def maria():
    return "Hello, Maria"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return (f"<h1>Hello, {name}!</h1>")

@app.route("/david")
def daivd():
    return "Hello, David"
