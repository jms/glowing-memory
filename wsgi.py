
from flask import Flask
from fortune import get_fortune

app = Flask(__name__)


@app.route("/")
def index():
    return '<pre>' + get_fortune() + '<pre>'