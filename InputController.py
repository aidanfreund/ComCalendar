from Operator import Operator
from RequestValidator import RequestValidator
from Task import Task
from Happening import Happening
from Profile import Profile
from Calendar import Calendar

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

        
        Getters and setters:
        +set_active_happening(id): Boolean
        +set_active_calendar(id):Boolean

        +get_happenings_string()
        +get_events_string()
        +get_tasks_string()
        +get_reminder_string()
        +get_event_string()
        +get_task_string()

        
        Update operator parameter names and design
   

    
    
    '''
    

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
        if RequestValidator.validate_edit_event(name, start_time, description, end_time, cls.active_happening):
            return Operator.edit_event(name, start_time, end_time, description, cls.active_happening)
        else:
            return False
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls):
        if RequestValidator.validate_delete_event(cls.active_happening):
            return Operator.delete_event(cls.active_happening,cls.active_calendar)
        else:
            return 
    
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
        return Operator.delete_calendar(cls.active_calendar)

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

        calendar_obj1, calendar_obj2 = None

        cal_list = cls.active_profile.get_calendars()

        num_calendars = len(cal_list)
        

        if RequestValidator.validate_compare_calendars(calendar1_id,calendar2_id,num_calendars):
        
            for i in range(num_calendars):

                if i is calendar1_id:
                    calendar_obj1 = cal_list[i]
                else:
                    if i is calendar2_id:
                        calendar_obj2 = cal_list[i]
                        
            if calendar_obj1 or calendar_obj2 is None:
                return "Failed to find calendars"
            
            return Operator.compare_calendars(calendar_obj1, calendar_obj2)
        else:
            return "Compare calendars IDs failed validation"
    
    # Combines calendars using calendars calendar id's in range 0-numCalendars (converted to real id), returns a calendar object
    @classmethod
    def aggregate_calendar(cls, calendar1_id, calendar2_id, name):

        calendar_obj1, calendar_obj2 = None

        cal_list = cls.active_profile.get_calendars()

        num_calendars = len(cal_list)

        if RequestValidator.validate_aggregate_calendar(calendar1_id,calendar2_id, num_calendars):

            for i in range(num_calendars):

                if i is calendar1_id:
                    calendar_obj1 = cal_list[i]
                else:
                    if i is calendar2_id:
                        calendar_obj2 = cal_list[i]
                        
            if calendar_obj1 or calendar_obj2 is None:
                return False
        
            return Operator.aggregate_calendar(name, calendar_obj1, calendar_obj2)
        else:
            return False
      

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time):
        if RequestValidator.validate_create_reminder(start_time):
            return Operator.create_reminder(start_time, cls.active_happening)
        else:
            return False


     # Filters calendar by events, returns a string of filtered events
    @classmethod
    def filter_calendar_by_events(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_events( start_date, end_date):
            Operator.filter_calendar_by_events(cls.active_calendar, start_date, end_date)
        else:
            return False

    # Filters calendar by tasks, returns a string of filtered events
    @classmethod
    def filter_calendar_by_tasks(cls, start_date, end_date):
        if RequestValidator.validate_filter_calendar_by_tasks(start_date, end_date):
            Operator.filter_calendar_by_tasks(cls.active_calendar, start_date, end_date)
        else:
            return False
    
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
            return Operator.remove_task(cls.active_happening, cls.active_calendar)
        else:
            return False


    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls,name, description, due_date, is_completed):
        if RequestValidator.validate_edit_task(name, description, due_date, cls.active_happening):
            return Operator.edit_task(name, description, due_date, cls.active_happening)
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
        return Operator.delete_profile(cls.active_profile)
     

    #logins in and sets active profile object and returns true if successful
    @classmethod
    def login(cls,username, password):
        if RequestValidator.validate_login(username, password):
            cls.active_profile = Operator.attempt_login(username, password)
            return isinstance(cls.active_profile, Profile)
        else:
            return False

    #Creates a profile obj, sets it to active, and returns true is successful
    @classmethod
    def create_profile(cls, username, password):
        if RequestValidator.validate_create_profile(username, password):
            cls.active_profile = Operator.create_profile(username, password)
            return isinstance(cls.active_profile, Profile)
        else:
            return False
        
    
    #UI controls

    

    def get_calendar_list(cls):

        message_str = ""

        if not cls.active_profile:
            message_str = "No active profile"
        else:
            message_str += "Calendar list:\n"
            cal_list = cls.active_profile
            for cal in cal_list:
                message_str += f"   {cal.get_calendar_id()}: {cal.get_calendar_name()}\n"

        return message_str


    def get_event_list(cls):
        message_str = ""

        if not cls.active_calendar:
            message_str = "No active calendar"
        else:
            message_str += "Event list:\n"
            event_list = cls.active_calendar.retrieve_events()
            for event in event_list:
                message_str += f"   {event.get_id()}: {event.get_name()}\n"

        return message_str
        

    def get_task_list(cls):
        message_str = ""

        if not cls.active_calendar:
            message_str = "No active calendar"
        else:
            message_str += "Task list:\n"
            task_list = cls.active_calendar.retrieve_tasks()
            for task in task_list:
                message_str += f"   {task.get_id()}: {task.get_name()}\n"

        return message_str


    def set_active_happening(cls,id):
        if isinstance(cls.active_calendar, Calendar):
            happ_list = cls.active_calendar.retrieve_events() + cls.active_calendar.retrieve_tasks()
            for happ in happ_list:
                if happ.get_id() is id:
                    cls.active_happening = happ
                    return True
            return False
        else:
            return False
        




    def set_active_calendar(cls,id):
        pass

    def get_happenings_string(cls):
        pass
    def get_events_string(cls):
        pass
    def get_tasks_string(cls):
        pass
    def get_reminder_string(cls):
        pass
    def get_event_string(cls):
        pass
    def get_task_string(cls):
        pass
