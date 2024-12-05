from Operator import Operator
from RequestValidator import RequestValidator

class InputController:

    active_profile = None
    active_calendar = None
    active_happening = None
    active_reminder = None
    #calendar

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, calendar_obj):
        if RequestValidator.validate_add_event(name, start_time, end_time):
            Operator.add_event(name, start_time, end_time, calendar_obj)
        else:
            raise Exception("Validation error occurred")

    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name, start_time, end_time, event_obj):
        if RequestValidator.validate_edit_event(name, start_time, end_time):
            Operator.edit_event(name, start_time, end_time, event_obj)
        else:
            raise Exception("Validation error occurred")
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls, event_obj, profile_obj):
        Operator.delete_event(event_obj, profile_obj)
    
    # Creates new calendar with name, returns true if successful
    @classmethod
    def create_calendar(cls, name, profile_obj):
        if RequestValidator.validate_create_calendar(name):
            Operator.create_calendar(name, profile_obj)
        else:
            raise Exception("Validation error occurred")
    
    # Deletes calendar 
    @classmethod
    def delete_calendar(cls, calendar_obj, profile_obj):
        Operator.create_calendar(calendar_obj, profile_obj)

    # Processes .ics file string and returns calendar object
    @classmethod
    def upload_calendar(cls, calendar_obj, profile_obj):
        Operator.upload_calendar(calendar_obj, profile_obj)
    
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls):
        pass

     # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls, calendar_obj, profile_obj):
        Operator.copy_calendar(calendar_obj, profile_obj)
       

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def compare_calendars(cls, calendar_id1, calendar_id2, start_time, end_time):
        if RequestValidator.validate_compare_calendars(calendar_id1, calendar_id2, start_time, end_time):
            Operator.compare_calendars(calendar_id1, calendar_id2, start_time, end_time)
        else:
            raise Exception("Validation error occurred")
    
    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def aggregate_calendar(cls, calendar_obj1, calendar_obj2):
        Operator.aggregate_calendar(calendar_obj1, calendar_obj2)
      

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time, happ_obj):
        if RequestValidator.validate_create_reminder(start_time):
            Operator.create_reminder(start_time, happ_obj)
        else:
            raise Exception("Validation error occurred")

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
        if RequestValidator.validate_filter_calendar_by_events(calendar_obj, start_date, end_date):
            Operator.filter_calendar_by_events(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")

    # Filters calendar by tasks, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_tasks(calendar_obj, start_date, end_date):
            Operator.filter_calendar_by_tasks(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")
    
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_dates(calendar_obj, start_date, end_date):
            Operator.filter_calendar_by_dates(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, description, due_date, calendar_obj):
        if RequestValidator.validate_add_task(description, due_date):
            Operator.add_task(description, due_date, calendar_obj)
        else:
            raise Exception("Validation error occurred")

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls, task_obj, calendar_obj):
        Operator.remove_task(task_obj, calendar_obj)


    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls, description, due_date, task_obj):
        if RequestValidator.validate_edit_task(description, due_date):
            Operator.edit_task(description, due_date, task_obj)
        else:
            raise Exception("Validation error occurred")
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls, reminder_obj, happ_obj):
        Operator.remove_reminder(reminder_obj, happ_obj)

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, reminder_id, new_time):
        if RequestValidator.validate_edit_reminder(reminder_id, new_time):
            Operator.edit_reminder(reminder_id, new_time)
        else:
            raise Exception("Validation error occurred")

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls, profile_obj):
        if RequestValidator.validate_delete_profile(profile_obj):
            Operator.delete_profile(profile_obj)
        else:
            raise Exception("Validation error occurred")

    #Logs in to profile using username and password
    #Returns profile obj if a match exists
    @classmethod
    def login(cls,username, password):
        if RequestValidator.validate_login(username, password):
            Operator.login(username, password)
        else:
            raise Exception("Validation error occurred")

    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        if RequestValidator.validate_login(username, password):
            Operator.create_profile(username, password)
        else:
            raise Exception("Validation error occurred")
        
