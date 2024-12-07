import re
import datetime
from Event import Event
from Task import Task

class RequestValidator:

    @staticmethod
    def validate_add_event(name, start_time, end_time, description):
        passed = isinstance(name,str) and isinstance(start_time,datetime) and isinstance(end_time,datetime) and isinstance(description,str)

        if not RequestValidator.__validate_name(name) or not RequestValidator.__validate_description(description):
            passed = False

        return passed
        

    @staticmethod
    def validate_edit_event(name, start_time, end_time, description, happ_obj):
        passed = RequestValidator.validate_add_event(name,start_time,end_time,description)
        
        if not isinstance(happ_obj,Event):
            passed = False

        return passed

    @staticmethod
    def validate_delete_event(happ_obj):
        return isinstance(happ_obj,Event)

    @staticmethod
    def validate_create_calendar(name):
        return RequestValidator.__validate_name(name)

    @staticmethod
    def validate_upload_calendar(file_path, name):
        return re.search("^((\/[a-zA-Z0-9-_]+)+|\/)$",file_path) and RequestValidator.__validate_name(name)

    @staticmethod
    def validate_create_reminder(start_time):
        return isinstance(start_time,datetime)

    @staticmethod
    def validate_filter_calendar_by_dates(start_date, end_date):
        return isinstance(start_date,datetime) and isinstance(end_date,datetime)

    @staticmethod
    def validate_add_task(name, description, due_date):
        isinstance(name,str) and isinstance(due_date,datetime) and isinstance(description,str)

    @staticmethod
    def validate_remove_task(happ_obj):
        pass

    @staticmethod
    def validate_edit_task(name, description, due_date, is_completed, happ_obj):
        pass

    @staticmethod
    def validate_edit_reminder(new_time):
        pass

    @staticmethod
    def validate_login(username, password):
        pass

    @staticmethod
    def validate_create_profile(username, password):
        pass

    @staticmethod
    def __validate_description(desc):
        return re.search("^[\w .,!]*$",desc)

    @staticmethod
    def __validate_name(name):
        return re.search("^[\w ]*$",name)


 