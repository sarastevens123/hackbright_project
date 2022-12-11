"""CRUD operations"""

from model import db, User, Restaurant, UserRating, RestaurantRating, connect_to_db

def create_user(fname, lname, password, email, profile_img):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, password=password, email=email, profile_img=profile_img)
    db.session.add(user)
    db.session.commit()
    
    return user

def create_restaurant(restaurant_name, email, restaurant_password, restaurant_address, profile_img):
    """Create and return a new restaurant."""

    restaurant = Restaurant(restaurant_name=restaurant_name, email=email, restaurant_password=restaurant_password, restaurant_address=restaurant_address, profile_img=profile_img)
    db.session.add(restaurant)
    db.session.commit()

    return restaurant

def log_in_user(email, password):
    """Logs a user into their account"""

    

def return_all_users():
    """"Return a list of all users."""

    return User.query.all()

def return_all_restaurants():
    """"Return a list of all restaurants."""

    return Restaurant.query.all()

def return_user_by_id(user_id):
    """"Returns a user by their ID."""

    return User.query.get(user_id)

def return_restaurant_by_id(restaurant_id):
    """"Returns a restaurant by its ID."""

    return Restaurant.query.get(restaurant_id)

def get_user_by_email(email):
    """Return a user by their email, else returns None."""

    return User.query.filter(User.email == email).first()

def get_restaurant_by_email(email):
    """Return a restaurant by their email, else returns None."""

    return Restaurant.query.filter(Restaurant.email == email).first()

def get_user_password(password):
    """Return User password."""

    return User.query.filter(User.password == password).first()

def get_restaurant_password(restaurant_password):
    """Return restaurant password."""

    return Restaurant.query.filter(Restaurant.restaurant_password == restaurant_password).first()

def create_restaurant_rating(user_id, restaurant_id, rating_score, rating_text, rating_img):
    """Creates and returns a restaurant rating."""
    
    rating = RestaurantRating(user_id=user_id, restaurant_id=restaurant_id, rating_score=rating_score, rating_text=rating_text, rating_img=rating_img)
    db.session.add(rating)
    db.session.commit()
    
    return rating

def create_user_rating(restaurant_id, user_id, rating_score, rating_text, rating_img):
    """Creates and returns a user rating."""

    rating = UserRating(restaurant_id=restaurant_id, user_id=user_id, rating_score=rating_score, rating_text=rating_text, rating_img=rating_img)
    db.session.add(rating)
    db.session.commit()

    return rating

def get_average_rest_score(restaurant_id):

    total_scores = 0
    counter = RestaurantRating.query.filter_by(restaurant_id=restaurant_id).count()

    if counter > 0:
        ratings = RestaurantRating.query.filter_by(restaurant_id=restaurant_id).all()

        for rating in ratings:
            total_scores = total_scores + int(rating.rating_score)

        average_score = total_scores / counter

        return ("{:.1f}".format(average_score))


def get_average_guest_score(user_id):

    total_scores = 0
    counter = User.query.filter_by(user_id=user_id).count()

    if counter > 0:
        ratings = User.query.filter_by(user_id=user_id).all()

        for rating in ratings:
            total_scores = total_scores + int(rating.rating_score)
        
        average_score = total_scores / counter

        return ("{:.1f}".format(average_score))


if __name__ == '__main__':
    from server import app
    connect_to_db(app)