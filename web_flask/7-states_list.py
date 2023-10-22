#!/usr/bin/python3
'''This script starts a web application
The listens on 0.0.0.0, port 5000
'''
from flask import Flask
from models import storage
from flask import render_template


app = Flask(__name__)
'''Route is defined with strict_slashes=False'''


@app.teardown_appcontext
def close_db(error):
    '''removes the current SQLAlchemy Session'''
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    '''fetches dat from storage and displays as a HTML page'''
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    '''listen on 0.0.0.0 port 5000'''
    app.run(host="0.0.0.0", port=5000)
