# Exercise number 1 on the flask API course

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Now we will do a route with a decorator.
# A decorator is code that you can wrap around methods or classes.
'''
@app.route('/') # With a slash we say its our root.
def hello():
    return "Hey Flask"
'''

# Applying the SQL Lite table
# We will tell flask where the app is located so it places the embeded database correctly
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

# We create database object and the marshmallow object
db = SQLAlchemy(app)
ma = Marshmallow(app)

# With this we created the "schema"

# The Guide class is going to have 2 columns
class Guide(db.Model): # We call the Model method inside the db object
    id = db.Column(db.Integer, primary_key=True) # We stablish the primary key, an unique ID that automatically increments.
    title = db.Column(db.String(100), unique=False) # as you can see we first stablish the type and the total length, and then we stablish whetjher it will be unique or not.
    content = db.Column(db.String(144), unique=False)

    # Now we have the schema, but we need a constructor:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class GuideSchema(ma.Schema):
    class Meta: # We embed the metadata and we set the fields
        fields = ('title', 'content')

# Let's initiate the schema, first for single elements and then multiple
guide_schema = GuideSchema()
guides_schema = GuideSchema(many=True)

if __name__ == '__main__':
    app.run(debug=True)

