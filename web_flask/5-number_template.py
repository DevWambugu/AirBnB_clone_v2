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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display “HBNB!”'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''display “C ” followed by the value of the text variable'''
    formatted_text = text.replace("_", " ")
    return "C " + formatted_text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    '''display “Python ”, followed by the value of the text variable'''
    formatted_text = text.replace("_", " ")
    return "Python " + formatted_text


@app.route('/number/<int:n>', strict_slashes=False)
def check_int(n):
    '''display “n is a number” only if n is an integer'''
    return f"{n} is a number"


@app.route('/number/<int:n>', strict_slashes=False)
def HTML_int(n):
    '''Displays a HTML output if n is an integer'''
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    '''listen on 0.0.0.0 port 5000'''
    app.run(host="0.0.0.0", port=5000)
