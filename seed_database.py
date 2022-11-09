import os
import json

import crud
import model
import server

os.system("dropdb db_name")
os.system("createdb db_name")

model.connect_to_db(server.app)
