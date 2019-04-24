from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/sup")
def hellos():
    return "<h1>sup, dude!</h1>"

if __name__ == "__main__":
    app.run()