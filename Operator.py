from Profile import Profile
from Calendar import Calendar
from Happening import Happening
from Event import Event
from Task import Task
from Reminder import Reminder
from DBFactory import DatabaseFactory,FactoryProducer
from DBProfile import DB_Profile







class Operator:

    factory:DatabaseFactory = FactoryProducer("Profile")
    db_profile:DB_Profile = factory.DB_profile

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, description, calendar_obj):
        new_event_id = cls.db_profile.add_event(description,start_time,end_time,name,calendar_obj)
        if new_event_id is not -1:
            calendar_obj.add_event(Event(new_event_id,name,start_time,end_time,description))
            return True
        else:
            return False
  

    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name, start_time, end_time, description, event_obj):
        pass
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls, event_obj, calendar_obj):
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
    def upload_calendar(cls, file_path, name, profile_obj):
        pass
    
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls, calendar_obj):
        pass

     # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls, calendar_obj, profile_obj):
        pass

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def compare_calendars(cls, calendar_obj1, calendar_obj2):
        pass
    
    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def aggregate_calendar(cls, calendar_obj1, calendar_obj2):
        pass

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time, happ_obj):
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
    def attempt_login(cls,username, password):
        pass


    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        pass
        