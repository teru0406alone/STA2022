
from flask import flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('Hello.html')
