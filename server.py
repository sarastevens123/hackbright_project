"""Server for user/restaurants ratings app."""

from flask import (Flask, render_template, request, flash, session, flask_login,
                    redirect)
from model import connect_to_db, db, UserRating, User, Restaurant, RestaurantRating
import crud
from jinja2 import StrictUndefined

from flask_login import LoginManager
login_manager = LoginManager()

login_manager.init_app(app)


app = Flask(__name__)
app.secret_key = "b20e627e21b804e38201ea694f15973e63443d94c4bf7ae4c2c7b5ed99add345"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Display the homepage"""

    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def handle_guest_login():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)

    if password == user.password:
        session['user'] = user.user_id
        flash('Login successful!')

        return redirect('/profile')

    else:
        flash('User not found')
        create_new = input('Would you like to create a new account?')

        if create_new == 'Yes':
            return redirect('/create')


@app.route('/create', methods=['POST'])
def create_new_user():
    return



@app.route('/profile')
def display_profile():
    return 






    


    