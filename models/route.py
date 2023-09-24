# Importing necessary modules
from app import app, db
from app import Restaurant, Pizza, restaurant_pizza
from flask import request, jsonify
from datetime import datetime

# Define routes

# Route to get all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])