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

@app.route('/restaurants')
def list_restaurants():
    """Shows restauarants that a guest can review""" 

    restaurant_list = crud.return_all_restaurants()  
    print(restaurant_list)

    return render_template('all_restaurants.html', restaurant_list=restaurant_list)   


@app.route('/guest-signup', methods=['POST', 'GET'])
def signup_new_guest():
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        profile_image = request.form.get('profile-image')

        user = crud.create_user(fname=first_name, password=password,lname=last_name, email=email, profile_img = profile_image)
       

        session['user'] = user.user_id
        
        flash("Account created. You are now logged in.")


    return render_template('guest-signup-form.html')

@app.route('/restaurant-signup', methods=['POST', 'GET'])
def signup_new_restaurant():

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        address = request.form.get('address')
        profile_image = request.form.get('profile-image')

        user = crud.create_restaurant(restaurant_name=name, restaurant_password=password, email=email, restaurant_address=address, profile_img=profile_image)


        session['user'] = user.restaurant_id

        flash("Account created. You are now logged in.")

        return redirect('/')


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
            print(user.fname, user.lname)
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
            print(user.restaurant_name)
            return render_template('home.html')
       

        #user password does not exist in guest accounts
        flash("user password does not match")
        return render_template ('restaurant-login.html')
    else:
        return render_template('restaurant-login.html') 

@app.route('/user')
def user():

    if session['user']:
        print('**********USER IN SESSION**********')
        print(session['user'])
    else:
        print('No user in session')

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



# @app.route('/restaurants')
# def list_restaurants():
#     """Shows restauarants that a guest can review""" 

#     restaurant_list = crud.return_all_restaurants()  
#     print(restaurant_list)

#     return render_template('all_restaurants.html', restaurant_list=restaurant_list)   

@app.route('/restaurant/<restaurant_id>')
def show_restaurant(restaurant_id):
    """Return page showing the details of a given restaurant.

    It'll show all the info about the restaurant as well as provide a button to review them"""

    restaurant = crud.return_restaurant_by_id(restaurant_id)
    print(restaurant)
    
    return render_template('restaurant-details.html', restaurant=restaurant)


@app.route('/log-out')
def log_out_user():
    """Logs a user out and resets the session"""

    session['user'] = None
    session.modified = True
    print('you have been logged out')

    flash('You have been logged out!')

    return redirect('/')






if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )



    


    