import os
import json

#import crud
import model
import server

os.system("dropdb kickback_database")
os.system("createdb kickback_database")

model.connect_to_db(server.app)
model.db.create_all()