
from abc import ABC
import pymysql

#abstract database connection class
class DatabaseConnection(ABC):
    def get_db_connection(self):
        pass

#implementation of MySQL database connection
class MySQLConnection(DatabaseConnection):
    __SQL_connection = None

    #private init only called on first creation of a connection
    def ___init__():
        print("SQL connection created")

    #singleton pattern to get the singleton connection
    def get_db_connection():
        if(MySQLConnection.__SQL_connection == None):
            MySQLConnection.__SQL_connection = MySQLConnection.__create_mySQL_connection("localhost","Colton","IT326GroupProject","MySQL")
            MySQLConnection.___init__()
            return MySQLConnection.__SQL_connection
        else:
            return MySQLConnection.__SQL_connection
        
    #private helper to create connection to mySQL
    def __create_mySQL_connection(host_name, user_name, password_in, db_name):
        connection = None
        try:
            connection = pymysql.connect(
                host = host_name,
                user = user_name,
                password = password_in,
                database = db_name
            )
            print("Connection successful")
        except Exception as err:
            print(f"The error '{err}' occured")
        return connection