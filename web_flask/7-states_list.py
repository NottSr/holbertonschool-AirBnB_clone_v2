#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def C_is_(text):
    C_space = text.replace('_', ' ')
    return "C {}".format(C_space)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


@app.route('/states_list', strict_slashes=False)
def states_list():
    str_state = storage.all(State).values()
    return render_template('7-states_list.html', str_state=str_state)


@app.teardown_appcontext
def td_app(var):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
