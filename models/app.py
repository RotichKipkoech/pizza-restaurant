# Importing necessary modules
from flask import Flask, request, jsonify, make_response
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint