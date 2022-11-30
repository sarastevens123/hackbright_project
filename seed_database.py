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

    