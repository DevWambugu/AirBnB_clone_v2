#!/usr/bin/python3
'''This script starts a web application
The listens on 0.0.0.0, port 5000
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


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


@app.route("/states", strict_slashes=False)
def states():
    '''displays with the list of all State objects
    present in DBStorage sorted by name (A->Z)
    '''
    states = storage.all(State).values()
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    '''finds state with the ID'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html",
                                   state=state, state_cities=state.cities)
        return render_template('9-states.html', not_found=True)


@app.route("/hbnb_filters", strict_slashes=False)
def html_page():
    '''Displays a HTML page'''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    cities = list()
    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template('10-hbnb_filters.html',
                           states=states, state_cities=cities,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    '''remove the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    '''listen on 0.0.0.0 port 5000'''
    app.run(host="0.0.0.0", port=5000)
