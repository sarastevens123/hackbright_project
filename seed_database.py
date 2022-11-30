import os


import crud
import model
import server

os.system("dropdb kickback_database")
os.system("createdb kickback_database")

if __name__ == "__main__":
    
    model.connect_to_db(server.app)
    server.app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= True
    


    model.db.create_all()

    user = crud.create_user('sarah', 'stevens', 'password', 'email', 'img')
    model.db.session.add(user)
    model.db.session.commit()

    restaurant = crud.create_restaurant('name', 'email', 'password', '112 address', 'img')
    model.db.session.add(restaurant)
    model.db.session.commit()

    user_review = crud.create_user_rating(user.user_id, restaurant.restaurant_id, '5', 'text', 'img')
    model.db.session.add(user_review)
    model.db.session.commit()

    restaurant_review = crud.create_restaurant_rating(user.user_id, restaurant.restaurant_id, '3', 'text', 'img')
    model.db.session.add(restaurant_review)
    model.db.session.commit()