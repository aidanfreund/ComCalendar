
from abc import ABC
from DBConnection import MySQLConnection
from DBProfile import MySQLProfile

#abstract factory
class Database_factory(ABC):

    def _create_db_connection(self):
        pass

    def _create_profile_controller(self):
        pass


class SQL_factory(Database_factory):
    def __init__(self):
        self.DB_connection = SQL_factory.__create_db_connection()
        self.DB_profile = SQL_factory.__create_profile_controller()

    def __create_db_connection(self):
        return MySQLConnection.get_db_connection()
    
    def _create_profile_controller(self):
        return MySQLProfile.get_DB_profile()
    
class FactoryProducer():
    def __init__(self, functionality):
        if(functionality == "MySQL"):
            return SQL_factory()
        else:
            print("Enter correct type of factory to create")
