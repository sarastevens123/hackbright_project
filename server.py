"""Server for user/restaurants ratings app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect )
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, UserRating, User, Restaurant, RestaurantRating
import crud
from jinja2 import StrictUndefined




app = Flask(__name__)


app.secret_key = "b20e627e21b804e38201ea694f15973e63443d94c4bf7ae4c2c7b5ed99add345"
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db.init_app(app)

@app.route('/')
def home():
    """Display the homepage"""

    return render_template('index.html')


@app.route('/user-signup', methods=['POST', 'GET'])
def signup_new_user():
    
    if request.form.get(id) == 'user-signup':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        profile_image = request.form.get('profile-image')

        user = crud.create_user(fname=first_name, password=password,lname=last_name, email=email, profile_img = profile_image)
        db.session.add(user)
        db.session.commit()
        flash("Account created. Please log in.")

    return render_template('user-signup.html')

@app.route('/restaurant-signup', methods=['POST', 'GET'])
def signup_new_restaurant():

    if request.form.get == 'restaurant-signup':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        address = request.form.get('address')
        profile_image = request.form.get('profile-image')

        restaurant = crud.create_restaurant(restaurant_name=name, restaurant_password=password, email=email, restaurant_address=address, profile_img=profile_image)
        db.session.add(restaurant)
        db.session.commit()
    flash("Account created. Please log in.")

    return render_template('restaurant-signup.html')


@app.route('/login', methods=['POST', 'GET'])
def handle_guest_login():
    print('hello')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_user_by_email(email)
        if user is None:
            flash("User not found. Please create an account")
            return render_template('login.html')
        if password == user.password:
            session['user'] = user
            flash('Login successful')
            return redirect('/profile')

        #user password does not exist
        flash("user password does not match")
        return render_template ('login.html')
    else:
        return render_template('login.html') 


@app.route('/user-rating', methods=['POST', 'GET'])
def submit_user_rating():

    guest = request.form.get('guest')
    restaurant = request.form.get('restaurant')
    score = request.form.get('score')
    review = request.form.get('review')
    image = request.form.get('image')
    # the column is user_id i need it to take in a guest name.
    rating = crud.create_user_rating( restaurant_id=restaurant, rating_score=score, rating_text=review, rating_img=image, user_id=guest)
    db.session.add(rating)
    db.session.commit()

    
@app.route('/restaurant-rating', methods=['POST', 'GET'])
def submit_restaurant_rating():

    restaurant = request.form.get('restaurant')
    score = request.form.get('score')
    review = request.form.get('review')
    image = request.form.get('image')
    # the column is restaurant_id i need it to take in a restaurant name.
    rating = crud.create_restaurant_rating( rating_score=score, rating_text=review, rating_img=image, restaurant_id=restaurant)
    db.session.add(rating)
    db.session.commit()
     







if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )



    


    