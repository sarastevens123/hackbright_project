"""Server for user/restaurants ratings app."""

from flask import (Flask, render_template, request, flash, session, 
                    redirect)
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "saras_project"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Display the homepage"""

    return render_template('homepage.html')

    