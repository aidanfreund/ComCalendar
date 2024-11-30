
from DBConnection import MySQLConnection
from DBProfile import MySQLProfile

db_connection = MySQLConnection.get_db_connection()
if(db_connection != None):
    print("Working")

db_profile = MySQLProfile.get_db_profile()
result = db_profile.add_profile("abcd", "aaa",db_connection)
if result > 0:
    print("Add profile Working")

