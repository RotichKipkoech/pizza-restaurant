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

# Route to get a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is not None:
        pizzas = [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        return jsonify({'id': restaurant.id, 'name': restaurant.name, 'address': restaurant.address, 'pizzas': pizzas})
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    
# Route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is not None:
        restaurant_pizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404
    
# Route to get all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

# Route to create a new RestaurantPizza
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (price and 1 <= price <= 30 and pizza_id and restaurant_id):
        return jsonify({'errors': ['Validation errors']}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if restaurant is None or pizza is None:
        return jsonify({'errors': ['Invalid pizza or restaurant ID']}), 400

    try:
        restaurant_pizza = restaurant_pizza(price=price, restaurant=restaurant, pizza=pizza)
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'errors': ['RestaurantPizza already exists']}), 400