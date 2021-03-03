import sys
import json
from functions.database import *

""" Connect to database usin config/config.json """

config_file = open('config/config.json')
config_data = json.load(config_file)

host_db     = config_data['database']['host']
database_db = config_data['database']['database']
user_db     = config_data['database']['username']
password_db = config_data['database']['password']
port_db     = config_data['database']['port']

db_connect(host_db, user_db, password_db, port_db, database_db)