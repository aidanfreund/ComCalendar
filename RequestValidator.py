from Operator import Operator
from Calendar import Calendar
from datetime import datetime


class RequestValidator:
    
   
    #Check for invalid event id's, invalid return


    @classmethod
    def validate_login(cls, username, password):
        return isinstance(username,str) and isinstance(password,str)


    @classmethod
    def validate_add_event(cls, event_id, name, start_time, end_time, calendar):
        if not (isinstance(event_id,int) and isinstance(name,str) and isinstance(start_time,datetime) and isinstance(end_time,datetime) and isinstance(calendar,Calendar)):
            return False
        if calendar.get_calendar_ID() is -1:
            return False
        

    @classmethod
    def validate_edit_event(cls, event_id, old_name, new_name, start_time, end_time, calendar):
        if not isinstance(event_id,int):
            return False
        if not isinstance(old_name,str):
            return False
        if not isinstance(new_name,str):
            return False
        if not isinstance(start_time,datetime):
            return False
        if not isinstance(end_time,datetime):
            return False
        if not isinstance(calendar,Calendar):
            return False
        if calendar.get_calendar_ID() or event_id is -1:
            return False
        return True

    @classmethod
    def validate_delete_event(cls, event_id, calendar):
        if not isinstance(event_id,int):
            return False
        if not isinstance(calendar,Calendar):
            return False
        if calendar.get_calendar_ID or event_id is -1:
            return False
        return True

    @classmethod
    def validate_create_calendar(cls,calendar_id, name):
        if not isinstance(calendar_id,int):
            return False
        if not isinstance(calendar_name,str):
            return False
        if event_id is -1:
            return False
        return True

    @classmethod
    def validate_delete_calendar(cls, calendar_id):
        if calendar_id is -1:
            return False
        return True

    @classmethod
    def validate_upload_calendar(cls, ics_contents):
        return type(ics_contents) is str
            
    @classmethod
    def validate_aggregate_calendar(cls, calendar1, calendar2):
        return type(calendar1) and type(calendar2) is Calendar

    @classmethod
    def validate_create_reminder(cls, reminder_id, reminder_time):
        if reminder_id is -1:
            return False

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
    def validate_change_reminder(cls, reminder_id, new_time):
        pass

    @classmethod
    def validate_delete_profile(cls, user_id):
        pass
    
    @classmethod
    def validate_filter_by_dates(cls, calendar, start_time, end_time):
        pass

    # Returns true if string contains no invalid chars
    @classmethod
    def __check_permitted_chars(cls,str):
        for char in str:
            if char not in cls.total_chars:
                return False 
        return True

