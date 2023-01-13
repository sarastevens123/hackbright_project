"""Server for user/restaurants ratings app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect, url_for )
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, db, Restaurant, User
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
    if session['user']:
        user_id= int(session['user'])
        guest_user = crud.return_user_by_id((user_id))
        return render_template('guest-home.html',guest_user=guest_user.fname, user_ratings=guest_user.user_ratings)
     
    else:
        return render_template('login-route-page.html', )


@app.route('/restaurant-home')
def restaurant_home():
    """Display the homepage"""

    if session['user']:
        restaurant_id= int(session['user'])
        user = crud.return_restaurant_by_id((restaurant_id))
        print(user)
        print(user.restaurant_ratings)
        return render_template('restaurant-home.html',user=user.restaurant_name, restaurant_ratings=user.restaurant_ratings)
    else:
        return render_template('login-route-page.html', )

@app.route('/restaurants')
def list_restaurants():
    """Shows restaurants that a guest can review""" 

    restaurant_list = crud.return_all_restaurants()  
    print(restaurant_list)

    return render_template('all_restaurants.html', restaurant_list=restaurant_list)   

@app.route('/restaurant/<restaurant_id>')
def show_restaurant(restaurant_id):
    """Return page showing the details of a given restaurant.

    It'll show all the info about the restaurant as well as provide a button to review them"""

    restaurant = crud.return_restaurant_by_id(restaurant_id)
    
    print(restaurant)
    average_score = crud.get_average_rest_score(restaurant_id)
    return render_template('restaurant-details.html', restaurant=restaurant, average_score=average_score)

@app.route('/guests')
def list_guests():
    """Shows guests that can be reviewed by a restaurant"""

    guest_list = crud.return_all_users()
    print(guest_list)

    return render_template('all-guests.html', guest_list=guest_list)

@app.route('/guest/<user_id>')
def show_guest(user_id):
    """Return page showing the details of a given guest.
    
    It'll show all the info about a guest as well as provide a button to review them"""

    guest = crud.return_user_by_id(user_id)
    print(guest)
    average_score= crud.get_average_guest_score(user_id)
    
    return render_template('guest-details.html', guest=guest, average_score=average_score)

@app.route('/guest-signup', methods=['POST', 'GET'])
def signup_new_guest():
    "Creates new guest account, adds that data to the database, logs the guest into the session"
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        profile_image = request.form.get('profile-image')

        user = crud.create_user(fname=first_name, password=password,lname=last_name, email=email, profile_img = profile_image)
       
        session['user'] = user.user_id
        
        flash("Account created. You are now logged in.")

        return redirect('/')

    return render_template('guest-signup-form.html')

@app.route('/restaurant-signup', methods=['POST', 'GET'])
def signup_new_restaurant():
    """Creates new restaurant account, adds restaurant data to database, logs the restaurant into the session"""

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')
        address = request.form.get('address')
        profile_image = request.form.get('profile-image')

    

        user = crud.create_restaurant(restaurant_name=name, restaurant_password=password, email=email, restaurant_address=address, profile_img=profile_image)


        session['user'] = user.restaurant_id

       

        return redirect('/restaurant-home')


    return render_template('restaurant-signup.html')


@app.route('/guest-login', methods=['POST', 'GET'])
def log_in_guest():
    """Log's in a user that is a guest"""
    
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
           
            print(user.fname, user.lname)
            return redirect('/')

        #user password does not exist in guest accounts
        flash("user password does not match")
        return render_template ('guest-login.html')
    else:
        return render_template('guest-login.html') 


@app.route('/restaurant-login', methods=['POST', 'GET'])
def log_in_restaurant():
    """Logs in a restaurant"""
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = crud.get_restaurant_by_email(email)
        print(user, user.restaurant_ratings)
       
        #checks to see if there is a restaurant account by email
        if user is None:
            flash("Restaurant account not found. Try again or create an account")
            return render_template('restaurant-login.html')

        # checks if the password is linked to the user
        if password == user.restaurant_password:
            session['user'] = user.restaurant_id
            print(session['user'])
            #return render_template('restaurant-home.html',user=user.restaurant_name, restaurant_ratings=user.restaurant_ratings)
            return redirect('/restaurant-home')
       

#         #user password does not exist in restaurant accounts
        flash("user password does not match")
        return render_template ('restaurant-login.html')
    else:
        return render_template('restaurant-login.html') 
    

# # @app.route('/user')
# def user():
#     """Shows the user in the session"""

#     if session['user']:
#         print('**********USER IN SESSION**********')
#         print(session['user'])
#     else:
#         print('No user in session')

#     return redirect('/')


@app.route('/user-rating', methods=['POST', 'GET'])
def submit_user_rating():
    """adds a user rating"""

    print(request.args)
    user_id=None
    
    if request.args:
        user_id = int(request.args.get('user_id'))
        
    if request.form.get == 'user-rating':
        guest = request.form.get('guest')
        restaurant = request.form.get('restaurant')
        score = request.form.get('score')
        review = request.form.get('review')
        image = request.form.get('image')

        rating = crud.create_user_rating( restaurant_id=restaurant, rating_score=score, rating_text=review, rating_img=image, user_id=guest)
        db.session.add(rating)
        db.session.commit()
        return redirect('/restaurant-home')

    return render_template('user-rating-form.html', users=User.query, user_id=user_id)
        
@app.route('/restaurant-rating/<restaurant_id>', methods=['POST', 'GET'])
@app.route('/restaurant-rating', methods=['POST', 'GET'])
def submit_restaurant_rating(restaurant_id=None):
    """adds a restaurant rating"""
    
    
    user_id= int(session['user'])
    restaurant_id = int(restaurant_id) if restaurant_id else restaurant_id

    if request.method == 'POST':
        
        restaurant_id = int(request.form.get('restaurant'))
        score = int(request.form.get('score'))
        review = request.form.get('review')
        image = request.form.get('image')
        print(request.form)

        #restaurant_id = crud.get_rest_id_by_name(restaurant)
        rating = crud.create_restaurant_rating(user_id=user_id, restaurant_id=restaurant_id, rating_score=score, rating_text=review, rating_img=image)
        db.session.add(rating)
        db.session.commit()

        
    return render_template('restaurant-rating-form.html', restaurants=Restaurant.query, restaurant_id=restaurant_id)

@app.route('/reviews')
def show_reviews_of_user():
    """shows a logged in user the reviews made about them"""

    

    return 




@app.route('/log-out')
def log_out_user():
    """Logs a user out and resets the session"""

    session['user'] = None
    session.modified = True
    print('You have been logged out')

    flash('You have been logged out!')

    return render_template('logged-out.html')






if __name__ == "__main__":
    connect_to_db(app)
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )



    


    