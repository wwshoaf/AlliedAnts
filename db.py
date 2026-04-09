## Write db.py connection helper
## get_connection() with DB_CONFIG · used by every module

import mysql.connector
from mysql.connector import Error

# Databse connection settings
# set this to your own local settings
# or you can make a new local db in mysql with the same settings
# we will change this to a .env file later if we make github repo public, shouldnt matter too much though if you have your sql set so there is no remote in
DB_CONFIG = {
    "host": "localhost",
    "user": "allied_ant",
    "password": "AlliedAnts4321!",
    "database": "440_project"
}

# try to connect to the database
def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
        return None
    except Error as e:
        print(f"Error in connecting to MySQL: {e}")
        return None
    
# Runs INSERT, UPDATE, DELETE type queries and returns a cursor
def execute_query(query, params = None):
    conn = get_connection()

    # if connection fails
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        conn.commit()
        return cursor
    except Error as e:
        print(f"[DB Error] Query failed: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()

# Runs SELECT queries and returns list of tuples
# use to select multiple rows from each table
def fetch_all(query, params = None):
    conn = get_connection()

    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()
    except Error as e:
        print(f"[DB Error] Query failed: {e}")
        return None
    finally:
        conn.close()

# Runs SELECT query and returns one tuple
# Use to select one row from a specific table
def fetch_one(query, params = None):
    conn = get_connection()

    if not conn:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchone()
    except Error as e:
        print(f"[DB Error] Query failed: {e}")
        return None
    finally:
        conn.close()


