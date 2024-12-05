from Profile import Profile
from Calendar import Calendar
from DBFactory import FactoryProducer, Database_factory 
from DBProfile import DB_Profile
from DBConnection import Database_Connection
from CalendarFilter import CalendarFilter



class Operator:

    factory:Database_factory = FactoryProducer("Profile")
    db_connection:Database_Connection = factory.DB_Connection
    db_profile:DB_Profile = factory.DB_profile

    if db_connection is None:
        raise Exception('Failed to connect to database')
    
    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, calendar_obj):
        pass

    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name, start_time, end_time, event_obj):
        pass
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls, event_obj, profile_obj):
        pass
    
    # Creates new calendar with name, returns true if successful
    @classmethod
    def create_calendar(cls, name, profile_obj):
        pass
    
    # Deletes calendar 
    @classmethod
    def delete_calendar(cls, calendar_obj, profile_obj):
        pass

    # Processes .ics file string and returns calendar object
    @classmethod
    def upload_calendar(cls, calendar_obj, profile_obj):
        pass
    
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls):
        pass

     # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls, calendar_obj, profile_obj):
        pass

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def compare_calendars(cls, calendar_id1, calendar_id2, start_time, end_time):
        pass
    
    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def aggregate_calendar(cls, calendar_obj1, calendar_obj2):
        pass

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time, happ_obj):
        pass

    # To be discussed
    @classmethod
    def retrieve_calendar(cls, calendar_id):
        pass

    # To be discussed
    @classmethod
    def retrieve_event_information(cls, event_id, calendar_obj):
        pass

    # To be discussed
    @classmethod
    def retrieve_task_information(cls, task_id, calendar_obj):
        pass

     # Filters calendar by events, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_events(cls, calendar_obj, start_date, end_date):
        pass


    # Filters calendar by tasks, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj, start_date, end_date):
        pass
    
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        pass

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, description, due_date, calendar_obj):
        pass

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls, task_obj, calendar_obj):
        pass

    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls, description, due_date, task_obj):
        pass
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls, reminder_obj, happ_obj):
        pass

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, reminder_obj, new_time):
        pass

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls, profile_obj):
        pass

   
    #Logs in to profile using username and password
    #Returns profile obj if a match exists
    @classmethod
    def login(cls,username, password):
        pass


    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        pass
        