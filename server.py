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

    return render_template('home.html')


@app.route('/guest-signup', methods=['POST', 'GET'])
def signup_new_guest():
    
    if request.form.get(id) == 'guest-signup-form':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        profile_image = request.form.get('profile-image')

        user = crud.create_user(fname=first_name, password=password,lname=last_name, email=email, profile_img = profile_image)
        db.session.add(user)
        db.session.commit()

        session['user'] = user.user_id
        
        flash("Account created. You are now logged in.")


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


@app.route('/guest-login', methods=['POST', 'GET'])
def log_in_guest():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_user_by_email(email)
        
       

        #checks to see if there is a guest account by email
        if user is None:
            flash("Guest account not found. Please create an account")
            return render_template('guest-login.html')

        # checks if the password is linked to the user
        if password == user.password:
            session['user'] = user.user_id
            flash('Login successful')
            return render_template('home.html')

        #user password does not exist in guest accounts
        flash("user password does not match")
        return render_template ('guest-login.html')
    else:
        return render_template('guest-login.html') 


@app.route('/restaurant-login', methods=['POST', 'GET'])
def log_in_restaurant():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_restaurant_by_email(email)
       

        #checks to see if there is a restaurant account by email
        if user is None:
            flash("Restaurant account not found. Please create an account")
            return render_template('login.html')

        # checks if the password is linked to the user
        if password == user.restaurant_password:
            session['user'] = user.restaurant_id
            flash('Login successful')
            return render_template('home.html')
       

        #user password does not exist in guest accounts
        flash("user password does not match")
        return render_template ('restaurant-login.html')
    else:
        return render_template('restaurant-login.html') 

@app.route('/user')
def user():

    if session['user']:
        print('**********here it is**********')

    return redirect('/')


@app.route('/user-rating', methods=['POST', 'GET'])
def submit_user_rating():

    if request.form.get == 'user-rating':
        guest = request.form.get('guest')
        restaurant = request.form.get('restaurant')
        score = request.form.get('score')
        review = request.form.get('review')
        image = request.form.get('image')

        rating = crud.create_user_rating( restaurant_id=restaurant, rating_score=score, rating_text=review, rating_img=image, user_id=guest)
        db.session.add(rating)
        db.session.commit()


    return render_template('user-rating-form.html')
        
@app.route('/restaurant-rating', methods=['POST', 'GET'])
def submit_restaurant_rating():

    if request.form.get == 'restaurant-rating':
        restaurant = request.form.get('restaurant')
        score = request.form.get('score')
        review = request.form.get('review')
        image = request.form.get('image')

        rating = crud.create_restaurant_rating( rating_score=score, rating_text=review, rating_img=image, restaurant_id=restaurant)
        db.session.add(rating)
        db.session.commit()
    

    return render_template('restaurant-rating-form.html')
        







if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )



    


    