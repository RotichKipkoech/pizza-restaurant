## Pizza Restaurant Project

### AUTHOR
#### KENNEDY ROTTICH

### DESCRIPTION
Welcome to the Pizza Restaurant project! This project is a Flask API that manages Pizza Restaurants. It allows you to perform various operations related to restaurants and pizzas.

## Table of Contents

    Getting Started
        Prerequisites
        Installation
    Features
    Routes
    Models
    Running the Application
    Testing with Postman
    Contributing
    License

## Getting Started
### Prerequisites

Before you begin, ensure you have the following installed:

    * Python 3.8 and above
    * Flask
    * SQLAlchemy
    * SQLite

### Installation

    Clone the repository:

    * git clone git@github.com:RotichKipkoech/pizza-restaurant.git

Install the required packages:

    * pipenv --python 3.11
    * pipenv install
    * pipenv shell
    * pipenv  install Flask
    * pipenv install Flask-SQLAlchemy
    * pipenv install flask-restfull


### Features

    Create Restaurants: Add new pizza restaurants with a unique name and address.
    List Restaurants: Retrieve a list of all pizza restaurants.
    Get Restaurant Details: Retrieve details of a specific restaurant, including its pizzas.
    Delete Restaurants: Remove a restaurant and associated restaurant-pizza relationships.
    List Pizzas: Get a list of all available pizzas.
    Create Restaurant-Pizza Relationship: Associate a pizza with a restaurant along with a price.

### Routes

    GET /restaurants: Get a list of all restaurants.
    GET /restaurants/<id>: Get details of a specific restaurant.
    DELETE /restaurants/<id>: Delete a restaurant by ID.
    GET /pizzas: Get a list of all pizzas.
    POST /restaurant_pizzas: Create a new RestaurantPizza relationship.

## Models

### Restaurant

    Attributes:
        id (Integer, Primary Key)
        name (String, Unique, Not Null)
        address (String, Not Null)

### Pizza

    Attributes:
        id (Integer, Primary Key)
        name (String, Not Null)
        ingredients (String, Not Null)
        created_at (DateTime, Default: Current UTC time)
        updated_at (DateTime, Default: Current UTC time)

### RestaurantPizza

    Attributes:
        id (Integer, Primary Key)
        price (Integer, Not Null)
        restaurant_id (Integer, Foreign Key)
        pizza_id (Integer, Foreign Key)
        created_at (DateTime, Default: Current UTC time)
        updated_at (DateTime, Default: Current UTC time)

## Running the Application

    Ensure you have installed the prerequisites.

### Run the application:

    * python3 models/app.py
    * python3 models/routes.py

    * The server will start at http://localhost:5000.

### Testing with Postman

You can use Postman to test the API endpoints. Import the provided Postman collection and start testing.

## Contributing

Contributions are welcome! Fork the project, make your changes, and create a pull request.

## License

This project is licensed under the MIT License.