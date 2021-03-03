import mysql.connector
from mysql.connector import Error
import pandas as pd



""" Connect to database """
def db_connect(host, username, password, port, database):
    connection = None

    try:
        connection = mysql.connector.connect(
            host    = host,
            user    = username,
            passwd  = password,
            port    = port
        )
    except Error as err:
        print(f"Error: '{err}'")

    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        if (x[0] == database):
            return connection
    init_database(connection, database)



""" Initialize database """
def init_database(connection, database):
    execute_query(connection, "CREATE DATABASE " + database)



""" Execute a query """
def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
    except Error as err:
        print(f"Error: '{err}'")