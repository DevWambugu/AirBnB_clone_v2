#!/usr/bin/python3
'''This script starts a web application
The listens on 0.0.0.0, port 5000
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    ''' load all cities of a State'''
    states = storage.all(State).values()
    cities = list()

    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template("8-cities_by_states.html", states=states,
                           state_cities=cities)


@app.teardown_appcontext
def teardown(exc):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    '''listen on 0.0.0.0 port 5000'''
    app.run(host="0.0.0.0", port=5000)
