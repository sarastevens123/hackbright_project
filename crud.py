"""CRUD operations"""

from model import db, User, Restaurant, User_rating, Restaurant_rating, connect_to_db

def create_user(email, user_password):
    """Create and return a new user."""

    user = User(email=email, user_password=user_password)

    return user

def create_restaurant(email, restaurant_password):
    """Create and return a new restaurant."""

    restaurant = Restaurant(email=email, restaurant_password=restaurant_password)

    return restaurant

def return_all_users():
    """"Return a list of all users."""

    return User.query.all()

def return_all_restaurants():
    """"Return a list of all restaurants."""

    return User.query.all()

def return_user_by_id(user_id):
    """"Returns a user by their ID."""

    return User.query.get(user_id)

def return_restaurant_by_id(restaurant_id):
    """"Returns a restaurants by their ID."""

    return Restaurant.query.get(restaurant_id)

def get_user_by_email(email):
    """Return a user by their email, else returns None."""

    return User.query.filter(User.email == email).first()

def get_restaurant_by_email(email):
    """Return a restaurant by their email, else returns None."""

    return Restaurant.query.filter(Restaurant.email == email).first()

def get_user_password(user_password):
    """Return User password."""

    return User.query.filter(User.user_password == user_password).first()

def get_restaurant_password(restaurant_password):
    """Return restaurant password."""

    return Restaurant.query.filter(Restaurant.restaurant_password == restaurant_password).first()

def create_restaurant_rating():
    """Creates and returns a restaurant rating."""
    
    rating = Restaurant_rating()

    return rating

def create_user_rating():
    """Creates and returns a user rating."""

    rating = User_rating()


    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)