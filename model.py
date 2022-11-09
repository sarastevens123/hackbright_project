from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    fname = db.Column(db.Varchar(25), nullable=False)
    lname = db.Colum(db.Varchar(25), nullable=False)
    password = db.Colum(db.Varchar(10), nullable=False)
    email = db.Colum(db.Varchar(25), nullable=False)
    birth_date = db.Colum(db.Date, nullable=False)
    city = db.Colum(db.Varchar(25), nullable=False)
    user_since = db.Column(db.Timestamp, nullable=False)
    review_count = db.Column(db.Integer)
    score = db.Column(db.Integer)

    user_ratings = db.relationship("UserRating")
    restaurant_ratings= db.relationship("RestaurantRating")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname}>"



class Restaurant(db.model):
    """Data model for a restaurant"""

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    external_id = db.Column(db.Integer)
    restaurant_name = db.Column(db.Varchar(50), nullable=False)
    email = db.Column(db.Varchar(50), nullable=False)
    restaurant_password = db.Column(db.Varchar(10), nullable=False)
    restaurant_address = db.Column(db.Varchar(25), nullable=False)
    restaurant_state = db.Column(db.Varchar(25), nullable=False)
    city = db.Column(db.Varchar(25), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    review_count = db.Column(db.Integer)
    score = db.Column(db.Integer)
    
    restaurant_ratings = db.relationship("RestaurantRating")
    user_ratings = db.relationship("UserRating")


    def __repr__(self):
        return f"<Restaurant restaurant_id={self.restaurant_id} restaurant_name={self.restaurant_name}>"

class RestaurantRating(db.model):
    """Data model for restaurants rating"""

    __tablename__ = "restaurant_ratings"

    rating_id = db.Colum(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    rating_score = db.Column(db.Integer, nullable=False)
    rating_text = db.Column(db.Text)

    restaurant = db.relationship("Restaurant")
    user = db.relationship("User")


    def __repr__(self):
        return f"<Restaurant_rating rating_id={self.rating_id} score{self.rating_score}>"
    

class UserRating(db.model):
    """Data model for user ratings"""

    __tablename__ = "user_ratings"

    rating_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.restaurant_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),nullable=False)
    rating_score = db.Column(db.Integer, nullable=False)
    rating_text = db.Column(db.Text, nullable=False)

    restaurant = db.relationship("Restaurant")
    user = db.relationship("User")


    def __repr__ (self):
        return f"<User_rating rating_id={self.rating_id} score={self.score}>"


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///database"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")



if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)
    db.create_all()