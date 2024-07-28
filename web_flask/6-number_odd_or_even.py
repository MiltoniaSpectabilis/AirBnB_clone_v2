#!/usr/bin/python3
"""
Flask web application that displays various messages based on the URL path.
"""
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route function to display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route function to display "HBNB"
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route function to display "C " followed by the value of the text variable,
    replacing underscore _ symbols with a space.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route function to display "Python " followed by the value of
    the text variable, replacing underscore _ symbols with a space.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route function to display "n is a number" only if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route function to display an HTML page with "Number: n" inside the H1 tag.
    """
    # if isinstance(n, int):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route function to display an HTML page with
    "Number: n is even|odd" inside the H1 tag.
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
