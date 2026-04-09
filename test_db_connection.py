# Use this file to test the database connection
from db import get_connection

conn = get_connection()

if conn:
    print("connected")
    conn.close()
else:
    print('connection failed')
    