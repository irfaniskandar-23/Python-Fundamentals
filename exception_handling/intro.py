'''
Exception handling in python

try:
    statement
except:
    catch Exception BaseException
else:
    statement if no exception raised

finally:
     statement that executes regardless of try/except block result
'''
'''
in this simple example we will try to make a connection to a localhost database
implementing the try/block feature to handle any issue raised by Python
'''

# print(f"{type(error).__name__} was raised")    //to output the exception class for better handling


import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
DATABASE = {
    "host": 'localhost',
    'name': 'test_api',
    'username': "root",
    'password': 'root'
}
host = DATABASE['host']
name = DATABASE['name']
username = DATABASE['username']
password = DATABASE['password']


try:
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@{host}/{name}')

    connection = engine.connect()

except sqlalchemy.exc.OperationalError as error:
    print(f"{type(error).__name__} was raised")
    print(f"error: {error}")
else:
    df = pd.read_sql_query('''
    SELECT * FROM users
    ''', connection)

    print(df)
