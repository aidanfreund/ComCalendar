
from abc import ABC
import pymysql
import pymysql.cursors
from Calendar import Calendar
from Profile import Profile
from Happening import Happening
from Task import Task
from Event import Event

class DB_Profile(ABC):
    
    def add_calendar(self, calendar, profile, connection):
        pass
    
    def read_calendar(self,calendar_id, connection):
        pass

    def change_calendar(self, calendar, connection):
        pass

    def delete_calendar(self, calendar, connection):
        pass

    def read_task(self,task, connection):
        pass

    def delete_task(self, task, connection):
        pass
    
    def change_task(self, task, connection):
        pass

    def add_task(self, task, calendar, connection):
        pass
    
    def read_event(self,event, connection):
        pass

    def delete_event(self, event, connection):
        pass

    def change_event(self, event, connection):
        pass

    def add_event(self, start_time,end_time,description,name, calendar, connection):
        pass

    def change_profile_credentials(self, profile, connection):
        pass

    def delete_profile(self, profile, connection):
        pass

    def read_profile(self, connection):
        pass

    def add_profile(self, username,password, connection):
        pass

    def get_DB_profile():
        pass



class MySQLProfile(DB_Profile):
    
    my_sql_profile = None

    def ___init__():
        MySQLProfile.my_sql_profile = MySQLProfile()
    #function that is used to retrieve the DB Profile object to use for database operations
    #returns DB Profile Object
    def get_DB_profile():
        if(MySQLProfile.my_sql_profile == None):
            MySQLProfile.___init__()
        return MySQLProfile.my_sql_profile
    #function that takes a calendar name and profile that the new calendar will be connected to
    #returns boolean based on success of adding the calendar to the database
    def add_calendar(self, calendar_name, profile, connection):
        if type(profile) is not Profile:
            print("passed profile object is not a Profile object")
            return -1
        try: #creates a cursor to perform functions with
            with connection.cursor() as cursor:
                #sql statement
                sql_statement = "INSERT INTO new_schema.calendars (user_id, name) VALUES (%s,%s)"
                #values to go into the sql statement
                values = (profile.get_profile_ID(), calendar_name)
                #executes sql statement using the values found above
                cursor.execute(sql_statement, values)
                #commits the changes to the database
                connection.commit()
                #gets the id for the calendar and returns it
                id = cursor.lastrowid
                return id
        except Exception as e:
            #rollback any changes because there was an error
            connection.rollback()
            print(f"Error: {e}")
            return -1
    #function that takes a Calendar object and DBConnection Object to obtain the Calendar from the database
    #returns Calendar object based on the attributes of the calendar in the database
    def read_calendar(self,calender, connection):
        if type(calendar) is not Calendar:
            print("Passed calendar is not Calendar object")
            return None
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                #sql statement to execute
                sql_statement = "Select * from new_schema.calendars where calendar_id = %s"
                #using the cursor executes the sql statement passing the calendar id as input
                cursor.execute(sql_statement,(calender.get_calendar_ID(),))
                #gets the first result of executed statement as a dictionary
                result = cursor.fetchone()
                #if there is a result that it fetched change to Calendar object and return it
                if result:
                    calendar = Calendar(result.get('calendar_id',),result.get('name',))
                    return calendar
                else:
                    print("No record found")
                    return None
        except pymysql.MySQLError as e:
            print("Error getting calendar")
            return None
    #function that takes a calendar object and database connection that will change the name of the calendar if it differs from the database
    #returns boolena based on success of change if there was a change needed
    def change_calendar(self, calendar, connection):
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                
                sql_statement = "Select * from new_schema.calendars where calendar_id = %s"

                cursor.execute(sql_statement,(calendar.get_calendar_id(),))

                result = cursor.fetchone()

                if result is None:
                    print("No calendar found with ID: {calendar.id}")
                    return None
                if result['name'] != calendar.get_name():
                    sql_statement2 ="Update new_schema.calendars Set name = %s where calendar_id = %s"
                    cursor.execute(sql_statement2,(calendar.get_name(),calendar.get_calendar_id()))
                    connection.commit()
                    return True
                else:
                    print("Nothing to change on calendar")
                    return False
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False
     #function that takes a calendar object and database connection that deletes the calendar passed from the database 
     # returns a boolean indicating success of deletion  
    def delete_calendar(self, calendar, connection):
        if type(calendar) is not Calendar:
            print("Calendar passed is not of type Calendar")
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.calendars where calendar_id = %s"

                cursor.execute(sql_statement,(calendar.get_calendar_ID(),))

                if cursor.rowcount > 0:
                    print("Calendar deleted")
                    connection.commit()
                    return True
                else:
                    print("No Calendar found to delete with same primary key")
                    return False
        except Exception as e:
            connection.rollback()
            print("Error: {e}")
            return False
    #function that takes a task and db connection that reads the information of the task from the database
    #returns Task object
    def read_task(self,task, connection):
        pass

    def delete_task(self, task, connection):
        if type(task) is not Task:
            print("Task passed is not type Task")
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.tasks where task_id = %s"

                cursor.execute(sql_statement,(task.get_id(),))

                if cursor.rowcount > 0:
                    print("Task deleted")
                    connection.commit()
                    return True
                else:
                    print("Failed to delete task")
                    return False
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False
        

    def change_task(self, task, connection):
        if type(task) is not Task:
            print("Task passed is not a Task object")
            return -1
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:

                sql_statement = "Select * from new_schema.tasks where task_id = %s"

                cursor.execute(sql_statement,(task.get_id(),))
                
                result = cursor.fetchone()

                if result is None:
                    print("No record found")
                    return -1
                
                if result['start_time'] != task.get_first_time():
                    sql_time_statement = "Update new_schema.tasks Set start_time = %s Where task_id = %s"
                    values = (task.get_first_time(),task.get_id())
                    cursor.execute(sql_time_statement,values)
                if result['completion_status'] != task.get_completion():
                    sql_completion_statement = "Update new_schema.tasks Set completion_status = %s Where task_id = %s"
                    values = (task.get_completion(), task.get_id())
                    cursor.execute(sql_completion_statement,values)
                if result['description'] != task.get_description():
                    sql_description_statement = "Update new_schema.tasks Set description = %s Where task_id = %s"
                    values = (task.get_description(),task.get_id())
                    cursor.execute(sql_description_statement,values)
                if result['name'] != task.get_name():
                    sql_name_statment = "Update new_schema.tasks Set name = %s Where task_id = %s"
                    values = (task.get_name(), task.get_id())
                    cursor.execute(sql_name_statment,values)
                connection.commit()
                return True
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False
    
    def add_task(self, description,time,name, calendar, connection):
        if type(calendar) is not Calendar:
            print("Passed calendar is not of type Calendar")
            return -1
        try:
            with connection.cursor() as cursor:

                sql_statment = "Insert into new_schema.tasks (calendar_id,start_time,description,completion_status,name) Values (%s,%s,%s,%s,%s)"

                values = (calendar.get_calendar_ID(),time,description,False,name)

                cursor.execute(sql_statment,values)

                connection.commit()

                id = cursor.lastrowid
                return id
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return -1
        
    def read_event(self,event, connection):
        pass

    def delete_event(self, event, connection):
        if type(event) is not Event:
            print("Event passed is not type Event")
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.events Where event_id = %s"

                cursor.execute(sql_statement,(event.get_id(),))

                if cursor.rowcount > 0:
                    print("Event deleted")
                    connection.commit()
                    return True
                else:
                    print("No event found to delete")
                    connection.rollback()
                    return False
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False

    def change_event(self, event, connection):
        if type(event) is not Event:
            print("Passed event is not type Event")
            return False
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_statement = "Select * from new_schema.events where event_id = %s"

                cursor.execute(sql_statement,(event.get_id(),))

                result = cursor.fetchone()

                if result['name'] != event.get_name():
                    sql_name_statement = "Update new_schema.events Set name = %s Where event_id = %s"
                    values = (event.get_name(),event.get_id())
                    cursor.execute(sql_name_statement,values)
                if result['start_time'] != event.get_first_time():
                    sql_first_time_statement = "Update new_schema.events Set start_time = %s Where event_id = %s"
                    values = (event.get_name(),event.get_id())
                    cursor.execute(sql_first_time_statement,values)
                if result['description'] != event.get_description():
                    sql_description_statement = "Update new_schema.events Set description = %s Where event_id = %s"
                    values = (event.get_description(),event.get_id())
                    cursor.execute(sql_description_statement,values)
                if result['end_time'] != event.get_end_time():
                    sql_end_time_statement = "Update new_schema.events Set description = %s where event_id = %s"
                    values = (event.get_end_time(),event.get_id())
                    cursor.execute(sql_end_time_statement,values)
                connection.commit()
                return True
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False
    

    def add_event(self, start_time,end_time,description,name, calendar, connection):
        if type(calendar) is not Calendar:
            print("Calendar passed is not type Calendar")
            return -1
        try:
            with connection.cursor() as cursor:

                sql_statement = "Insert into new_schema.events (start_time,end_time,description,name,calendar_id) Values (%s,%s,%s,%s,%s)"

                values = (start_time,end_time,description,name,calendar.get_calendar_ID())

                cursor.execute(sql_statement,values)

                connection.commit()
                id = cursor.lastrowid
                return id
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return -1
        
    def change_profile_credentials(self, profile, connection):
        if type(profile) is not Profile:
            print("Passed profile is not type Profile")
            return False
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:

                sql_statement= "Select * from new_schema.profiles where user_id = %s"

                cursor.execute(sql_statement,(profile.get_profile_ID(),))

                result = cursor.fetchone()

                if not result:
                    print("No profile exists with that ID")
                    connection.rollback()
                    return False
                if result['username'] != profile.get_user_name():
                    sql_username_statement = "Update new_schema.profiles Set username = %s where user_id = %s"
                    values = (profile.get_user_name(),profile.get_profile_ID())
                    cursor.execute(sql_username_statement,values)
                connection.commit()
                return True
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False

    def delete_profile(self, profile, connection):
        if type(profile) is not Profile:
            print("Profile parameter is not type Profile")
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.profiles where user_id = %s"

                cursor.execute(sql_statement,(profile.get_profile_ID(),))

                if cursor.rowcount > 0:
                    print("Deleted Profile")
                    connection.commit()
                    return True
                else:
                    print("No profile found to delete")
                    connection.rollback()
                    return False
        except Exception as e:
            print("Error: {e}")
            connection.rollback()
            return False



    #function that takes a username and password and creates a profile in the database
    #returns int that is the id for that profile
    def add_profile(self, username, password, connection):
        try:
            with connection.cursor() as cursor:
                #sql statment to be executed
                sql_statement = "Insert into new_schema.profiles (username, password) Values (%s,%s)"
                #tuple holding values to be input into sql statement
                values = (username, password)
                #executing sql statement based on sql statement and values
                cursor.execute(sql_statement,values)
                #commit the changes to the database
                connection.commit()
                #get the id to return
                id = cursor.lastrowid
                return id

        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
            #return -1 to indicate an error occured
            return -1