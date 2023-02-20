# hackbright_project
# <img src=/img/logo_transparent_background.png width="50%">
Welcome to Kickback, where a guest reviews a restaurant leaving a brief account of their experience with a score - in return the restaurant will respond with a counter review with of the same entries. Kickback app allows for a two way channel of reviewing in the dining experience and acheives transparency among restaurants of interaction with the guests. The long-term vision is to connect restaurants to other nearby restaurants and give them a channel to alert industry workers of unruly and banned guests in the neighborhood.
## About Me
Sara is a full stack engineer and graduate of Hackbright Academy with over 12 years in the Food and Beverage Industry.

## Contents
* [Tech Stack](#tech-stack)
* [Features](#features)
* [Future Development](#future)
* [Installation](#install)

## <a name="tech-stack"></a>Tech Stack
* Python
* Flask
* Jinja2
* PostgreSQL
* SQLAlchemy 
* HTML
* CSS
* Bootstrap

## <a name="features"></a>Welcome

![alt text](https://github.com/sarastevens123/hackbright_project/static/homepage.png "Displays homepage view")

#### Sign-up/log-in
In Kickback, a user can be either a guest or a restaurant. Different user types have unique access to the apps functionality. Once a guest or restaurant user is created - a query is made to my PostgreSQL database to check if the user exists. If it does not- the new user is then added and commited to my database. 

![alt text](https://github.com/sarastevens123/hackbright_project/static/sign-up-form.png "Displays sign-up form")

![alt text](https://github.com/sarastevens123/hackbright_project/static/log-in-form.png "Displays log-in form")


#### Restaurant Reviews
A guest has access to review a nearby restaurant that they have visited by leaving a brief account of their expereience and a score. This review is displayed to the restaurant user once they log in to their profile.

![alt text](https://github.com/sarastevens123/hackbright_project/static/dak-chicken-reviews.png "Displays restaurant profile with reviews")

![alt text](https://github.com/sarastevens123/hackbright_project/static/review-form.jpg "Displays restaurant review form")



####  Guest Reviews
Reviews that were made about the guest user are displayed once the guest user logs into their profile. They are unable to respond to the counter review and their average score is dependent on what the restaurants score them as.

![alt text](https://github.com/sarastevens123/hackbright_project/static/reviews-about-jane.png "Displays guest profile with reviews")



## <a name="future"></a>Future Development
The next planned feature for Kickback is adding the Google Placces api to automatically find nearby restaurants in San Francisco.

## <a name="install"></a>Installation
To run Kickback on your machine:

1) Install PostgreSQL

Clone or fork this repo:
```
https://github.com/sarastevens123/hackbright_project
```

Create and activate a virtual environment inside your Board Game Village directory:
```
virtualenv env
source env/bin/activate
```

Install the dependencies:
```
pip install -r requirements.txt
```



Set up the database:

```
createdb kickback_database
python3 model.py
python3 seed_database.py
```

Run the app:

```
python3 server.py
```

You can now navigate to 'localhost:5000/' to access Kickback.
