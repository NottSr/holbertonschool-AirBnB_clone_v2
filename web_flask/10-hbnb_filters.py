#!/usr/bin/python3
"""
Starts a Flask web app
"""

from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display a HTML page like 6-index.html from static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)

    return render_template(
        '10-hbnb_filters.html',
        states=states, state_cities=cities,
        amenities=amenities)


@app.teardown_appcontext
def teardown_db(exc):
    """After each request remove current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
