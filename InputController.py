from Operator import Operator
from RequestValidator import RequestValidator

class InputController:

    active_profile = None
    active_calendar = None
    active_happening = None
    active_reminder = None
    

    '''
        ToDo:

        ID list with names:
        +get_calendar_list():String
        +get_event_list(): String
        +get_task_list(): String

        
        +set_active_happening(id): Boolean
        +set_active_calendar(id):Boolean

        +get_happenings_string()
        +get_events_string()
        +get_tasks_string()
        +get_reminder_string()
        +get_event_string()
        +get_task_string()

        
        Update parameters and design
    
    
    '''
    

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, description):
        if RequestValidator.validate_add_event(name, start_time, end_time, description,):
            Operator.add_event(name, start_time, end_time, description, calendar_obj)
        else:
            raise Exception("Validation error occurred")

    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name, start_time, end_time, description):
        if RequestValidator.validate_edit_event(name, start_time, description, end_time):
            Operator.edit_event(name, start_time, end_time, description, event_obj)
        else:
            raise Exception("Validation error occurred")
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls):
        Operator.delete_event(event_obj, calendar_obj)
    
    # Creates new calendar with name, returns true if successful
    @classmethod
    def create_calendar(cls, name):
        if RequestValidator.validate_create_calendar(name):
            Operator.create_calendar(name, profile_obj)
        else:
            raise Exception("Validation error occurred")
    
    # Deletes calendar 
    @classmethod
    def delete_calendar(cls):
        Operator.create_calendar(calendar_obj, profile_obj)

    # Processes .ics file string and adds it to profile
    @classmethod
    def upload_calendar(cls,file_path, name):
        Operator.upload_calendar(calendar_obj, profile_obj)
    
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls):
        pass

     # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls):
        Operator.copy_calendar(calendar_obj, profile_obj)
       

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def compare_calendars(cls, start_time, end_time, calendar1_id, calendar2_id):
        if RequestValidator.validate_compare_calendars(start_time, end_time):
            Operator.compare_calendars(calendar_obj1, calendar_obj2, start_time, end_time)
        else:
            raise Exception("Validation error occurred")
    
    # Combines calendars, adds a new combined calendar to profile
    @classmethod
    def aggregate_calendar(cls, calendar1_id, calendar2_id, name):
        Operator.aggregate_calendar(name, calendar_obj1, calendar_obj2)
      

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time):
        if RequestValidator.validate_create_reminder(start_time):
            Operator.create_reminder(start_time, happ_obj)
        else:
            raise Exception("Validation error occurred")


     # Filters calendar by events, returns a string of filtered events
    @classmethod
    def filter_calendar_by_events(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_events( start_date, end_date):
            Operator.filter_calendar_by_events(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")

    # Filters calendar by tasks, returns a string of filtered events
    @classmethod
    def filter_calendar_by_tasks(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_tasks(start_date, end_date):
            Operator.filter_calendar_by_tasks(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")
    
     # Filters calendar by dates, returning a string of filtered events
    @classmethod
    def filter_calendar_by_dates(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_dates( start_date, end_date):
            Operator.filter_calendar_by_dates(calendar_obj, start_date, end_date)
        else:
            raise Exception("Validation error occurred")

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, description, due_date):
        if RequestValidator.validate_add_task(description, due_date):
            Operator.add_task(description, due_date, calendar_obj)
        else:
            raise Exception("Validation error occurred")

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls):
        Operator.remove_task(task_obj, calendar_obj)


    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls, description, due_date):
        if RequestValidator.validate_edit_task(description, due_date):
            Operator.edit_task(description, due_date, task_obj)
        else:
            raise Exception("Validation error occurred")
        
    # Marks a task as complete
    def complete_task(cls):
        pass
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls):
        Operator.remove_reminder(reminder_obj, happ_obj)

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, new_time):
        if RequestValidator.validate_edit_reminder(reminder_obj, new_time):
            Operator.edit_reminder(reminder_obj, new_time)
        else:
            raise Exception("Validation error occurred")

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls):
        Operator.delete_profile(profile_obj)
     

    #logins in and sets active profile object and returns true if successful
    @classmethod
    def login(cls,username, password):
        if RequestValidator.validate_login(username, password):
            Operator.login(username, password)
        else:
            raise Exception("Validation error occurred")

    #Creates a profile obj, sets it to active, and returns true is successful
    @classmethod
    def create_profile(cls, username, password):
        if RequestValidator.validate_login(username, password):
            Operator.create_profile(username, password)
        else:
            raise Exception("Validation error occurred")
        
