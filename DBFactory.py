
from abc import ABC
from DBConnection import MySQLConnection

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
        return MySQLConnection.Get_DB_connection()
    
class FactoryProducer():
    def __init__(self, functionality):
        if(functionality == "Profile"):
            return SQL_factory()
        else:
            print("Enter correct type of factory to create")
