# Importing necessary modules
from flask import Flask, request, jsonify, make_response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

# Creating a Flask application instance
app = Flask(__name__)

# Configuring the database URI
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///emp.db'

# Creating a SQLAlchemy instance and binding it to the Flask app
db = SQLAlchemy(app)