
from abc import ABC
import pymysql
import pymysql.cursors
from Calendar import Calendar
from Profile import Profile
from Task import Task
from Event import Event
from DBConnection import DatabaseConnection, MySQLConnection
import datetime
from Happening import Happening
from Reminder import Reminder

class DBProfile(ABC):
    
    def add_calendar(self, calendar_name, profile):
        pass
    
    def read_calendars(self,profile):
        pass

    def change_calendar(self, calendar):
        pass

    def delete_calendar(self, calendar):
        pass

    def read_tasks(self,calendar):
        pass

    def delete_task(self, task):
        pass
    
    def change_task(self, task):
        pass

    def add_task(self, description,time,name, calendar):
        pass
    
    def read_events(self,calendar):
        pass

    def delete_event(self, event):
        pass

    def change_event(self, event):
        pass

    def add_event(self,description, start_time,end_time,name, calendar):
        pass

    def delete_profile(self, profile):
        pass

    def add_profile(self, username,password):
        pass

    def add_reminder(self, time, happening):
        pass

    def delete_reminder(self,reminder):
        pass

    def change_reminder(self,reminder):
        pass

    def read_reminder(self,happening):
        pass

    def read_profile(self,username,password):
        pass

    def get_db_profile():
        pass



class MySQLProfile(DBProfile):
    
    my_sql_profile = None

    def ___init__():
        MySQLProfile.my_sql_profile = MySQLProfile()
    #function that is used to retrieve the DB Profile object to use for database operations
    #returns DB Profile Object
    def get_db_profile():
        if(MySQLProfile.my_sql_profile == None):
            MySQLProfile.___init__()
        return MySQLProfile.my_sql_profile
    #working
    #function that takes a calendar name and profile that the new calendar will be connected to
    #returns id of the calendar or -1 for error
    def add_calendar(self, calendar_name:str, profile:Profile):
        connection = MySQLConnection.get_db_connection()
        if type(profile) is not Profile:
            return -1
        try: #creates a cursor to perform functions with
            with connection.cursor() as cursor:
                #sql statement
                sql_statement = "INSERT INTO new_schema.calendars (user_id, name) VALUES (%s,%s)"
                #values to go into the sql statement

                values = (profile.get_profile_id(), calendar_name)
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
    #function that takes a Profile object and DBConnection Object to obtain the Calendars from the database associated with the profile
    #returns Calendar object array that holds calendars associated with the passed profile
    def read_calendars(self,profile:Profile):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_get_calendars_statement = "Select * from new_schema.calendars where user_id = %s"

                cursor.execute(sql_get_calendars_statement,(profile.get_profile_id(),))
                result = cursor.fetchall()

                if not result:
                    return []
                else:
                    calendar_array = []
                    for row in result:
                        calendar_array.append(Calendar(row['calendar_id'],row['name'],None,None))
                    return calendar_array
        except Exception as e:
            print(f"Error: {e}")
            return [] 
            
    #working
    #function that takes a calendar object and database connection that will change the name of the calendar if it differs from the database
    #returns boolean based on success of change if there was a change needed
    def change_calendar(self, calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                
                sql_statement = "Select * from new_schema.calendars where calendar_id = %s"

                cursor.execute(sql_statement,(calendar.get_calendar_id(),))

                result = cursor.fetchone()

                if result is None:
                    return False
                if result['name'] != calendar.get_calendar_name():
                    sql_statement2 ="Update new_schema.calendars Set name = %s where calendar_id = %s"
                    cursor.execute(sql_statement2,(calendar.get_calendar_name(),calendar.get_calendar_id()))
                    connection.commit()
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
    #working
    #function that takes a calendar object and database connection that deletes the calendar passed from the database 
    # returns a boolean indicating success of deletion  
    def delete_calendar(self, calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        if type(calendar) is not Calendar:
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.calendars where calendar_id = %s"

                cursor.execute(sql_statement,(calendar.get_calendar_id(),))

                if cursor.rowcount > 0:
                    connection.commit()
                    return True
                else:
                    return False
        except Exception as e:
            connection.rollback()
            print(f"Error: {e}")
            return False
    #function that takes a calendar object and db connection that gets all associated tasks to the calendar
    #returns Task object array corresponding to tasks associated with the calendar passed
    def read_tasks(self,calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_statement = "Select * from new_schema.tasks where calendar_id = %s"
                cursor.execute(sql_statement,(calendar.get_calendar_id(),))

                result = cursor.fetchall()
                if not result:
                    return []
                else:
                    task_array = []
                    for row in result:
                        task_array.append(Task(row['task_id'],row['name'],row['start_time'],row['description']))
                    return task_array
        except Exception as e:
            print(f"Error: {e}")
            return []
    #working
    #function that takes a Task object and DB connection object that deletes the passed task in the database
    #returns Boolean based on success of deletion
    def delete_task(self, task:Task):
        connection = MySQLConnection.get_db_connection()
        if type(task) is not Task:
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.tasks where task_id = %s"

                cursor.execute(sql_statement,(task.get_id(),))

                if cursor.rowcount > 0:
                    connection.commit()
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
    #working
    #function that takes a Task object and DB Connection object that changes the task in the databse based on the passed object
    #returns Boolean based on success of changes
    def change_task(self, task:Task):
        connection = MySQLConnection.get_db_connection()
        if type(task) is not Task:
            return False
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:

                sql_statement = "Select * from new_schema.tasks where task_id = %s"

                cursor.execute(sql_statement,(task.get_id(),))
                
                result = cursor.fetchone()

                if result is None:
                    return False
                
                if result['start_time'] != task.get_first_time():
                    sql_time_statement = "Update new_schema.tasks Set start_time = %s Where task_id = %s"
                    values = (task.get_first_time(),task.get_id())
                    cursor.execute(sql_time_statement,values)
                if result['completion_status'] != task.get_completed():
                    sql_completion_statement = "Update new_schema.tasks Set completion_status = %s Where task_id = %s"
                    values = (task.get_completed(), task.get_id())
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
            print(f"Error: {e}")
            connection.rollback()
            return False
    #working
    #function that takes string,datetime,string,Calendar object, and DB connection that adds a task to the database tying it to the calendar
    #returns the id of the newly added task or -1 for error
    def add_task(self, description:str,time:datetime,name:str, calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        if type(calendar) is not Calendar:
            return -1
        try:
            with connection.cursor() as cursor:

                sql_statment = "Insert into new_schema.tasks (calendar_id,start_time,description,completion_status,name) Values (%s,%s,%s,%s,%s)"

                values = (calendar.get_calendar_id(),time,description,False,name)

                cursor.execute(sql_statment,values)

                connection.commit()

                id = cursor.lastrowid
                return id
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return -1

    #function that takes a Calendar object and DB connection that gets all events associated with the calendar
    #returns Event object array
    def read_events(self,calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_statement = "Select * from new_schema.events where calendar_id = %s"
                cursor.execute(sql_statement,(calendar.get_calendar_id(),))

                result = cursor.fetchall()
                if not result:
                    return []
                else:
                    event_array = []
                    for row in result:
                        event_array.append(Event(row['event_id'],row['name'],row['start_time'],row['end_time'],row['description']))
                    return event_array
        except Exception as e:
            print(f"Error: {e}")
            return []



    #working
    #function that takes an Event object and DB connection Object that deletes the corresponding Event in the database
    #returns Boolean based on success of deletion
    def delete_event(self, event:Event):
        connection = MySQLConnection.get_db_connection()
        if type(event) is not Event:
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.events Where event_id = %s"

                cursor.execute(sql_statement,(event.get_id(),))

                if cursor.rowcount > 0:
                    connection.commit()
                    return True
                else:
                    connection.rollback()
                    return False
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
    #working
    #function that takes an Event object and DB Connection that changes the Event in the database based on the passed Event
    #returns Boolean based on success of changing the Event
    def change_event(self, event:Event):
        connection = MySQLConnection.get_db_connection()
        if type(event) is not Event:
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
                    values = (event.get_first_time(),event.get_id())
                    cursor.execute(sql_first_time_statement,values)
                if result['description'] != event.get_description():
                    sql_description_statement = "Update new_schema.events Set description = %s Where event_id = %s"
                    values = (event.get_description(),event.get_id())
                    cursor.execute(sql_description_statement,values)
                if result['end_time'] != event.get_second_time():
                    sql_end_time_statement = "Update new_schema.events Set end_time = %s where event_id = %s"
                    values = (event.get_second_time(),event.get_id())
                    cursor.execute(sql_end_time_statement,values)
                connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False
    #working
    #function that takes string,datetime,datetime,string,Calendar object, and DB Connection that adds and Event to the database tied to the calendar
    #returns the id of the Event or -1 for error
    def add_event(self,description:str, start_time:datetime,end_time:datetime,name:str, calendar:Calendar):
        connection = MySQLConnection.get_db_connection()
        if type(calendar) is not Calendar:
            return -1
        try:
            with connection.cursor() as cursor:

                sql_statement = "Insert into new_schema.events (start_time,end_time,description,name,calendar_id) Values (%s,%s,%s,%s,%s)"

                values = (start_time,end_time,description,name,calendar.get_calendar_id())

                cursor.execute(sql_statement,values)

                connection.commit()
                id = cursor.lastrowid
                return id
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return -1 

    #working
    #function that takes a profile Object and DB connection and deletes the passed profile from the database
    #returns Boolean based on success of deletion
    def delete_profile(self, profile:Profile):
        print(type(profile))
        connection = MySQLConnection.get_db_connection()
        if type(profile) is not Profile:
            print("Profile parameter is not type Profile")
            return False
        try:
            with connection.cursor() as cursor:

                sql_statement = "Delete from new_schema.profiles where user_id = %s"


                cursor.execute(sql_statement,(profile.get_profile_id(),))

                if cursor.rowcount > 0:
                    connection.commit()
                    return True
                else:
                    connection.rollback()
                    return False
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False

    #working
    #function that takes a username and password and creates a profile in the database
    #returns int that is the id for that profile
    def add_profile(self, username:str, password:str):
        connection = MySQLConnection.get_db_connection()
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
        
    def check_username_unique(self, username:str):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor() as cursor:

                sql_statement = "Select * from new_schema.profiles where username = %s"

                cursor.execute(sql_statement,(username,))

                result = cursor.fetchone()
                if result is None:
                    return True
                return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        

    def add_reminder(self,time:datetime,happening:Happening):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor() as cursor:
                if type(happening) is Task:
                    sql_statement = "Insert into new_schema.reminders (time, task_id, relationship_type) Values (%s,%s,%s)"

                    values = (time,happening.get_id(),"task")

                    cursor.execute(sql_statement,values)

                    result_id = cursor.lastrowid
                    if result_id > 0:
                        connection.commit()
                        return result_id
                    else:
                        connection.rollback()
                        return -1
                else:
                    sql_statement = "Insert into new_schema.reminders (time,event_id,relationship_type) Values (%s,%s,%s)"
                    values = (time,happening.get_id(),"event")
                    cursor.execute(sql_statement,values)

                    result_id = cursor.lastrowid
                    if result_id > 0:
                        connection.commit()
                        return result_id
                    else:
                        connection.rollback()
                        return -1
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return -1

    def change_reminder(self, reminder:Reminder):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_statement = "Select * from new_schema.reminders where reminder_id = %s"
                cursor.execute(sql_statement,(reminder.get_id(),))
                result = cursor.fetchone()

                if result['time'] != reminder.get_time():
                    sql_time_statement = "Update new_schema.reminders Set time = %s where reminder_id = %s"
                    cursor.execute(sql_time_statement,(reminder.get_time(),reminder.get_id()))
                connection.commit()
                return True
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False

    def delete_reminder(self, reminder:Reminder):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor() as cursor:
                sql_statement = "Delete from new_schema.reminders Where reminder_id = %s"
                cursor.execute(sql_statement,(reminder.get_id(),))

                if cursor.rowcount > 0:
                    connection.commit()
                    return True
                else:
                    connection.rollback()
                    return False
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
            return False

    def read_reminder(self,happening:Happening):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                if type(happening) is Task:
                    sql_statement = "Select * from new_schema.reminders where task_id = %s"
                    cursor.execute(sql_statement,(happening.get_id(),))
                    result = cursor.fetchone()
                    if result:
                        return Reminder(result['reminder_id'],result['time'])
                    else:
                        return None
                elif type(happening) is Event:
                    sql_statement = "Select * from new_schema.reminders where event_id = %s"
                    cursor.execute(sql_statement,(happening.get_id(),))

                    result = cursor.fetchone()
                    if result:
                        return Reminder(result['reminder_id'],result['time'])
                    else:
                        return None
        except Exception as e:
            print(f"Error: {e}")
            return None
                    
    def read_profile(self,username:str,password:str):
        connection = MySQLConnection.get_db_connection()
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql_statement = "Select * from new_schema.profiles Where username = %s and password = %s"
                cursor.execute(sql_statement,(username,password))

                result = cursor.fetchone()
                if result is None:
                    return None
                else:
                    return Profile(result['username'],result['user_id'],[])
        except Exception as e:
            print(f"Error: {e}")
            return None


