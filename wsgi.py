
from flask import Flask, render_template
from fortune import get_fortune

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', fortune=get_fortune())