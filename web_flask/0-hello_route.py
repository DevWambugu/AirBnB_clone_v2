#!/usr/bin/python3
'''This script starts a web application
The listens on 0.0.0.0, port 5000
'''
from flask import Flask


app = Flask(__name__)
'''Route is defined with strict_slashes=False'''


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''display “Hello HBNB!”'''
    return "Hello HBNB!"


if __name__ == "__main__":
    '''listen on 0.0.0.0 port 5000'''
    app.run(host="0.0.0.0", port=5000)
