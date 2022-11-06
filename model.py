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

    user_rating = db.relationships("User_ratings", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} fname={self.fname}>"



class Restaurant(db.model):
    """Data model for a restaurant"""

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    external_id = db.Column(db.Integer)
    name = db.Column(db.Varchar(25), nullable=False)
    email = db.Column(db.Varchar(25), nullable=False)
    password = db.Column(db.Varchar(10), nullable=False)
    address = db.Column(db.Varchar(25), nullable=False)
    state = db.Column(db.Varchar(25), nullable=False)
    city = db.Column(db.Varchar(25), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)
    review_count = db.Column(db.Integer)
    score =   
    
    restaurant_rating = db.relationships()
    

    
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
