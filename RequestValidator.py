from Operator import Operator
from Calendar import Calendar
from datetime import datetime


class RequestValidator:
    
    uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", "'", "\"", 
    ",", "<", ".", ">", "/", "?", "~", "`"
    ]
    spaces = [" "]

    total_chars = uppercase_letters + lowercase_letters + numbers + special_characters + spaces

    
    


    # Checks for:
    # username is within 3-30 characters
    # password 8-30 characters
    # no invalid chars
    @classmethod
    def validate_login(cls, username, password):
        if (3 < len(username) > 30 and 8 < len(password) > 30):
           return cls.__check_permitted_chars(username + password)
        else:    
            return False


    @classmethod
    def validate_add_event(cls, event_id, name, start_time, end_time, calendar):
        isValid = False
        
        if cls.__check_permitted_chars(name) is False:
            return False
        if calendar is None:
            return False
        
        

    @classmethod
    def validate_edit_event(cls, event_id, old_name, new_name, start_time, end_time, calendar):
        pass

    @classmethod
    def validate_delete_event(cls, event_id, calendar):
        pass

    @classmethod
    def validate_create_calendar(cls, user_id, calendar_name):
        pass

    @classmethod
    def validate_delete_calendar(cls, calendar_id):
        pass

    @classmethod
    def validate_upload_calendar(cls, calendar):
        pass

    @classmethod
    def validate_download_calendar(cls):
        pass

    @classmethod
    def validate_aggregate_calendar(cls, calendar1, calendar2):
        pass

    @classmethod
    def validate_create_reminder(cls, reminder_id, reminder_time):
        pass

    @classmethod
    def validate_retrieve_calendar(cls, calendar_id):
        pass

    @classmethod
    def validate_filter_calendar_by_events(cls, calendar, start_time, end_time):
        pass

    @classmethod
    def validate_retrieve_event_information(cls, event_id, calendar):
        pass

    @classmethod
    def validate_retrieve_task_information(cls, task_id, calendar):
        pass

    @classmethod
    def validate_filter_calendar_by_tasks(cls, calendar, start_time, end_time):
        pass

    @classmethod
    def validate_add_task(cls, task_id, name, due_date, calendar):
        pass

    @classmethod
    def validate_remove_task(cls, task_id, calendar):
        pass

    @classmethod
    def validate_edit_task(cls, task_id, old_name, new_name, due_date, calendar):
        pass

    @classmethod
    def validate_copy_calendar(cls, calendar_id):
        pass

    @classmethod
    def validate_compare_calendars(cls, calendar_id1, calendar_id2):
        pass

    @classmethod
    def validate_remove_reminder(cls, reminder_id):
        pass

    @classmethod
    def validate_edit_reminder(cls, reminder_id, new_time):
        pass

    @classmethod
    def validate_delete_profile(cls, user_id):
        pass
    
    @classmethod
    def validate_filter_calendar_by_dates(cls, calendar, start_time, end_time):
        pass

    # Returns true if string contains no invalid chars
    @classmethod
    def __check_permitted_chars(cls,str):
        for char in str:
            if char not in cls.total_chars:
                return False 
        return True

