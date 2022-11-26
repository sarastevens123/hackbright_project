"""Server for user/restaurants ratings app."""

from flask import (Flask, render_template, request, flash, session,
                    redirect)
from model import connect_to_db, db, UserRating, User, Restaurant, RestaurantRating
import crud
from jinja2 import StrictUndefined




app = Flask(__name__)
app.secret_key = "b20e627e21b804e38201ea694f15973e63443d94c4bf7ae4c2c7b5ed99add345"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def display_homepage():
    """Display the homepage"""

    return render_template('homepage.html')



@app.route('/sign-up', methods=['POST'])
def sign_up():
    """Creates a new user"""
    

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")






@app.route('/login', methods=['POST'])
def handle_guest_login():

    email = request.form.get('email')
    password = request.form.get('password')

    
    user = crud.get_user_by_email(email)

    for users in crud.return_all_users():
        if user in users:
            if password in crud.get_user_password():
                session['user'] = user
                flash('Login successful')
                return redirect('/profile')

        else:
            flash("User not found. Please create an account")
            return redirect('/login')

        

        

  


@app.route('/create', methods=['POST'])
def create_new_user():
    return



@app.route('/profile')
def display_profile():
    return 


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True,
    )



    


    