import mysql.connector
from mysql.connector import Error
import pandas as pd

""" Connect to database """
def db_connect(host, database, username, password, port):
    connection = None

    try:
        connection = mysql.connector.connect(
            host    = host,
            db      = database,
            user    = username,
            passwd  = password,
            port    = port
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection