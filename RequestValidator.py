from Operator import Operator
from Calendar import Calendar
from datetime import datetime


class RequestValidator:
    
   


    # Creates new event with attributes, returns true if successful
    @classmethod
    def validate_add_event(cls, name, start_time, end_time, calendar_obj):
        pass

    # Edits event, returns true if successful
    @classmethod
    def validate_edit_event(cls, name, start_time, end_time, event_obj):
        pass

    # Deletes event from calendar, returns true if successful
    @classmethod
    def validate_delete_event(cls, event_obj, profile_obj):
        pass

    # Creates new calendar with name, returns true if successful
    @classmethod
    def validate_create_calendar(cls, name, profile_obj):
        pass

    # Deletes calendar
    @classmethod
    def validate_delete_calendar(cls, calendar_obj, profile_obj):
        pass

    # Processes .ics file string and returns calendar object
    @classmethod
    def validate_upload_calendar(cls, file_path, name):
        pass

    # Returns .ics file string
    @classmethod
    def validate_download_calendar(cls):
        pass

    # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def validate_copy_calendar(cls, calendar_obj, profile_obj):
        pass

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def validate_compare_calendars(cls, calendar_id1, calendar_id2, start_time, end_time):
        pass

    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def validate_aggregate_calendar(cls, calendar_obj1, calendar_obj2):
        pass

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def validate_create_reminder(cls, start_time, happ_obj):
        pass

    # To be discussed
    @classmethod
    def validate_retrieve_calendar(cls, calendar_id):
        pass

    # To be discussed
    @classmethod
    def validate_retrieve_event_information(cls, event_id, calendar_obj):
        pass

    # To be discussed
    @classmethod
    def validate_retrieve_task_information(cls, task_id, calendar_obj):
        pass

    # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def validate_filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        pass

    # Adds task to a calendar, returns true if successful
    @classmethod
    def validate_add_task(cls, name, description, due_date):
        pass

    # Removes a task from calendar, returns true if successful
    @classmethod
    def validate_remove_task(cls, task_obj, calendar_obj):
        pass

    # Edits a task, returns true if successful
    @classmethod
    def validate_edit_task(cls, name, description, due_date, task_obj):
        pass

    # Removes reminder, returns true if successful
    @classmethod
    def validate_remove_reminder(cls, reminder_obj, happ_obj):
        pass

    # Edits a reminder object, returns true if successful
    @classmethod
    def validate_edit_reminder(cls, reminder_obj, new_time):
        pass

    # Deletes profile obj, returns true if successful
    @classmethod
    def validate_delete_profile(cls, profile_obj):
        pass

    # Logs in to profile using username and password
    # Returns profile obj if a match exists
    @classmethod
    def validate_login(cls, username, password):
        pass

    # Creates a profile obj and returns it
    @classmethod
    def validate_create_profile(cls, username, password):
        pass

