from Operator import Operator
from RequestValidator import RequestValidator
from Task import Task
from Happening import Happening
from Profile import Profile
from Calendar import Calendar
from Reminder import Reminder

class InputController:

    active_profile = None
    active_calendar = None
    active_happening = None
    active_reminder = None

    

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, description):
        if RequestValidator.validate_add_event(name, start_time, end_time, description):
            return Operator.add_event(name, start_time, end_time, description, cls.active_calendar)
        else:
            return False

    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name, start_time, end_time, description):
        if RequestValidator.validate_edit_event(name, start_time, end_time, description, cls.active_happening):
            return Operator.edit_event(name, start_time, end_time, description, cls.active_happening)
        else:
            return False
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls):
        if RequestValidator.validate_delete_event(cls.active_happening):
            passed = Operator.delete_event(cls.active_happening,cls.active_calendar)
            if passed:
                cls.active_happening = None
            return passed
        else:
            return False
    
    # Creates new calendar with name, returns true if successful
    @classmethod
    def create_calendar(cls, name):
        if RequestValidator.validate_create_calendar(name):
            return Operator.create_calendar(name, cls.active_profile)
        else:
            return False
    
    # Deletes calendar 
    @classmethod
    def delete_calendar(cls):
        passed = Operator.delete_calendar(cls.active_calendar,cls.active_profile)
        if passed:
            cls.active_calendar = None
        return passed

    # Processes .ics file string and adds it to profile
    @classmethod
    def upload_calendar(cls,file_path, name):
        if RequestValidator.validate_upload_calendar(file_path,name):
            return Operator.upload_calendar(file_path,name,cls.active_profile)
        
        
    
    # Returns downloads calendar to local directory
    @classmethod
    def download_calendar(cls):
        return Operator.download_calendar(cls.active_calendar)

    # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls):
        return Operator.copy_calendar(cls.active_calendar, cls.active_profile)
       

    # Compares calendars using calendars calendar id's in range 0-numCalendars (converted to real id), returns a calendar object, returns string of free times
    @classmethod
    def compare_calendars(cls, calendar1_id, calendar2_id):

        cal_list = cls.active_profile.get_calendars()

        calendar_obj1 = cal_list[calendar1_id]
        calendar_obj2 = cal_list[calendar2_id]
        
 
        if calendar_obj1 or calendar_obj2 is None:
            return "Failed to find calendars"
            
        return Operator.compare_calendars(calendar_obj1, calendar_obj2)
       
    
    # Combines calendars using calendars calendar id's in range 0-numCalendars (converted to real id), returns a calendar object
    @classmethod
    def aggregate_calendar(cls, calendar1_id, calendar2_id, name):

        cal_list = cls.active_profile.get_calendars()

        calendar_obj1 = cal_list[calendar1_id]
        calendar_obj2 = cal_list[calendar2_id]

        if calendar_obj1 or calendar_obj2 is None:
            return "Failed to find calendars"
            
        return Operator.aggregate_calendar(name, calendar_obj1, calendar_obj2)
      

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time):
        if RequestValidator.validate_create_reminder(start_time):
            return Operator.create_reminder(start_time, cls.active_happening)
        else:
            return False


     # Filters calendar by events, returns a string of filtered events
    @classmethod
    def filter_calendar_by_events(cls):
        event_array = Operator.filter_calendar_by_events(cls.active_calendar)
        result_string = ""
        i = 0
        for event in event_array:
            result_string += f"\n{i+1}.Event: {event.get_name()} Start Time: {event.get_first_time()} End Time: {event.get_second_time()} Description: {event.get_description()}"
            i += 1
        return result_string

    # Filters calendar by tasks, returns a string of filtered events
    @classmethod
    def filter_calendar_by_tasks(cls):
        task_array = Operator.filter_calendar_by_tasks(cls.active_calendar)
        result_string = ""
        i = 0
        for task in task_array:
            result_string += f"\n{i+1}.Task: {task.get_name()} Time: {task.get_first_time()} Description: {task.get_description()} Completion Status: {task.get_completed()}"
            i += 1
        return result_string
     # Filters calendar by dates, returning a string of filtered events
    @classmethod
    def filter_calendar_by_dates(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_dates( start_date, end_date):
            Operator.filter_calendar_by_dates(cls.active_calendar, start_date, end_date)
        else:
            return False

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, name, description, due_date):
        if RequestValidator.validate_add_task(name, description, due_date):
            return Operator.add_task(name, description, due_date, cls.active_calendar)
        else:
            return False

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls):
        if RequestValidator.validate_remove_task(cls.active_happening):
            passed = Operator.remove_task(cls.active_happening,cls.active_calendar)
            if passed:
                cls.active_happening = None
            return passed
        else:
            return False


    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls,name, description, due_date, is_completed):
        if RequestValidator.validate_edit_task(name, description, due_date, is_completed, cls.active_happening):
            return Operator.edit_task(name, description, due_date, is_completed, cls.active_happening)
        else:
            return False
        
    # Marks a task as complete, returns True is task is now completed (even if already was completed)
    def set_complete_task(cls):
        if isinstance(cls.active_happening,Task):
            if not cls.active_happening.get_completed():
                return Operator.edit_task()
        else:
            return False
                
            
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls):
        return Operator.remove_reminder(cls.active_happening._reminder,cls.active_happening)

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, new_time):
        if RequestValidator.validate_edit_reminder(new_time):
            return Operator.edit_reminder(cls.active_reminder, new_time)
        else:
            return False

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls):
        passed = Operator.delete_profile(cls.active_profile)
        if passed:
            cls.active_profile = None
        return passed
     

    #logins in and sets active profile object and returns true if successful
    @classmethod
    def login(cls,username, password):
        cls.active_profile = Operator.attempt_login(username, password)
        return isinstance(cls.active_profile, Profile)
        

    #Creates a profile obj, sets it to active, and returns true is successful
    @classmethod
    def create_profile(cls, username, password):
        if RequestValidator.validate_create_profile(username, password):
            cls.active_profile = Operator.create_profile(username, password)
            return isinstance(cls.active_profile, Profile)
        else:
            return False
        
    

    
    #Getters and setters

    
    @classmethod
    def get_profile(cls):
        return cls.active_profile

    @classmethod
    def get_calendar(cls):
        return cls.active_calendar

    @classmethod
    def get_happening(cls):
        return cls.active_happening

    @classmethod
    def get_reminder(cls):
        return cls.active_reminder

    @classmethod
    def set_calendar(cls, calendar_obj):
        cls.active_calendar = calendar_obj

    @classmethod
    def set_happening(cls, happ_obj):
        cls.active_happening = happ_obj

    @classmethod
    def set_reminder(cls, reminder_obj):
        cls.active_reminder = reminder_obj

