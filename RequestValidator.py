import re
from datetime import datetime
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
        if name is None or description is None or end_time is None or start_time is None or happ_obj is None:
            return False
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
        return isinstance(file_path,str) and RequestValidator.__validate_name(name)

    @staticmethod
    def validate_create_reminder(start_time):
        return isinstance(start_time,datetime)

    @staticmethod
    def validate_filter_calendar_by_dates(start_date, end_date):
        return isinstance(start_date,datetime) and isinstance(end_date,datetime)

    @staticmethod
    def validate_add_task(name, description, due_date):
        return isinstance(name,str) and isinstance(due_date,datetime) and isinstance(description,str)

    @staticmethod
    def validate_remove_task(happ_obj):
        return isinstance(happ_obj,Task)

    @staticmethod
    def validate_edit_task(name, description, due_date, is_completed, happ_obj):
        if name is None or description is None or due_date is None or is_completed is None or happ_obj is None:
            return False
        return RequestValidator.validate_add_task(name,description,due_date) and isinstance(is_completed,bool) and isinstance(happ_obj,Task)

    @staticmethod
    def validate_edit_reminder(new_time):
        return isinstance(new_time,datetime)

    @staticmethod
    def validate_create_profile(username, password):
        return re.search("^[a-zA-Z0-9]*$",username) is not None and re.search("^[a-zA-Z0-9]*$",password) is not None and username != "" and password != ""

    @staticmethod
    def __validate_description(desc):
        return re.search("^[\w .,!]*$",desc) is not None

    @staticmethod
    def __validate_name(name):
        return re.search("^[\w ]*$",name) is not None


 