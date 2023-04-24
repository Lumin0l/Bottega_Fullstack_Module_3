# Exercise number 1 on the flask API course

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Now we will do a route with a decorator.
# A decorator is code that you can wrap around methods or classes.

@app.route('/') # With a slash we say its our root.
def hello():
    return "Hey Flask"

if __name__ == '__main__':
    app.run(debug=True)

