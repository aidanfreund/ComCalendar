
from abc import ABC
from DBProfile import DB_Profile
from DBConnection import MySQLConnection

#abstract factory
class DatabaseFactory(ABC):

    def _create_db_connection(self):
        pass

    def _create_profile_controller(self):
        pass


class SQLFactory(DatabaseFactory):
    def __init__(self):
        SQLFactory.__create_db_connection()
        self.DB_profile = SQLFactory.__create_profile_controller()

    def __create_db_connection():
        MySQLConnection.get_db_connection()
    def __create_profile_controller():
        return DB_Profile.get_db_profile()

class FactoryProducer():
    def __init__(self, functionality):
        if(functionality == "Profile"):
            return SQLFactory()
        else:
            print("Enter correct type of factory to create")
