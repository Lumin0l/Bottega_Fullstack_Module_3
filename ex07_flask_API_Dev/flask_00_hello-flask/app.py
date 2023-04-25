# Exercise number 1 on the flask API course

from flask import Flask, request, jsonify # we added the second 2 to deal with the requests
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

# Now let's start making guides

# First of all, the decorator
@app.route('/guide', methods=["POST"]) # we are creating an end point with the verb (HTTP key) of 'Post'
def add_guide():
    # First we grab the values
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content) # we create a new var and we assign it the class with the values

    db.session.add(new_guide)
    db.session.commit() # this is a method that opens a route there and stores data

    guide = Guide.query.get(new_guide.id)

    return guide_schema.jsonify(guide)

# Endpoint to query all guides
@app.route("/guides", methods=["GET"])

def get_guides():
    all_guides = Guide.query.all()
    result = guides_schema.dump(all_guides)
    return jsonify(result.data)


# Endopoint for querying a single guide
@app.route("/guides/<id>", methods=["GET"])
def get_guide(id):
    guide = Guide.query.get(id)
    return guide_schema.jsonify(guide)

# Endopoint for updating a guide
@app.route("/guide/<id>", methods=["PUT"])
def guide_update(id):
    guide = Guide.query.get(id)
    title = request.json['title']
    content = request.json['content']

    guide.title = title
    guide.content = content

    db.session.commit()
    return guide_schema.jsonify(guide)

# Endpoint for deleting guide

# Endpoint for deleting a record
@app.route("/guide/<id>", methods=["DELETE"])
def guide_delete(id):
    guide = Guide.query.get(id)
    db.session.delete(guide)
    db.session.commit()

    return guide_schema.jsonify(guide)


if __name__ == '__main__':
    app.run(debug=True)

