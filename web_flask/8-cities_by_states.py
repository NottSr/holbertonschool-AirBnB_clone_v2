#!/usr/bin/python3
"""
States and State
"""
from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def routes():
    """Function that displays an HTML page"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exc):
    """After each request remove current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
