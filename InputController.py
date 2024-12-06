from Operator import Operator
from RequestValidator import RequestValidator

class InputController:

    profile = None
    calendar = None
    happening = None
    reminder = None

    @classmethod
    def add_event(cls, event_id, name, start_time, end_time, calendar):
        if(RequestValidator.validate_add_event(event_id,name,start_time,end_time,calendar)):
            Operator.add_event(event_id, name, start_time, end_time, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def edit_event(cls, event_id, new_name, new_description, start_time, end_time, calendar):
        if(RequestValidator.validate_edit_event(event_id, new_name, new_description, start_time, end_time, calendar)):
            Operator.edit_event(event_id, new_name, new_description, start_time, end_time, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def delete_event(cls, event_id, calendar):
        if(RequestValidator.validate_delete_event(event_id, calendar)):
            Operator.delete_event(event_id, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def create_calendar(cls, calendar_id, name):
        if(RequestValidator.validate_create_calendar(calendar_id, name)):
            Operator.create_calendar(calendar_id, name)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def delete_calendar(cls, calendar_id):
        if(RequestValidator.validate_delete_calendar(calendar_id)):
            Operator.delete_calendar(calendar_id)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def upload_calendar(cls, calendar):
        if(RequestValidator.validate_upload_calendar(calendar)):
            Operator.upload_calendar(calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def download_calendar(cls):
        if(RequestValidator.validate_download_calendar()):
            Operator.download_calendar()
        else:
            raise Exception("Validation error occured")

    @classmethod
    def aggregate_calendar(cls, calendar1, calendar2):
        if(RequestValidator.validate_aggregate_calendar(calendar1, calendar2)):
            Operator.aggregate_calendar(calendar1, calendar2)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def create_reminder(cls, reminder_id, time):
        if(RequestValidator.validate_create_reminder(reminder_id, time)):
            Operator.create_reminder(reminder_id, time)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def retrieve_calendar(cls, calendar_id):
        if(RequestValidator.validate_retrieve_calendar(calendar_id)):
            Operator.retrieve_calendar(calendar_id)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def filter_calendar_by_events(cls, calendar, start_time, end_time):
        if(RequestValidator.validate_filter_calendar_by_events(calendar, start_time, end_time)):
            Operator.filter_calendar_by_events(calendar, start_time, end_time)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def retrieve_event_information(cls, event_id, calendar):
        if(RequestValidator.validate_retrieve_event_information(event_id, calendar)):
            Operator.retrieve_event_information(event_id, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def retrieve_task_information(cls, task_id, calendar):
        if(RequestValidator.validate_retrieve_task_information(task_id, calendar)):
            Operator.retrieve_task_information(task_id, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def filter_calendar_by_tasks(cls, calendar, start_time, end_time):
        if(RequestValidator.validate_filter_calendar_by_tasks(calendar, start_time, end_time)):
            Operator.filter_calendar_by_tasks(calendar, start_time, end_time)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def add_task(cls, task_id, description, due_date, calendar):
        if(RequestValidator.validate_add_task(task_id, description, due_date, calendar)):
            Operator.add_task(task_id, description, due_date, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def remove_task(cls, task_id, calendar):
        if(RequestValidator.validate_remove_task(task_id, calendar)):
            Operator.remove_task(task_id, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def edit_task(cls, task_id, new_name, new_description, due_date, calendar):
        if(RequestValidator.validate_edit_task(task_id, new_name, new_description, due_date, calendar)):
            Operator.edit_task(task_id, new_name, new_description, due_date, calendar)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def copy_calendar(cls, calendar_id):
        if(RequestValidator.validate_copy_calendar(calendar_id)):
            Operator.copy_calendar(calendar_id)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def compare_calendars(cls, calendar_id1, calendar_id2):
        if(RequestValidator.validate_compare_calendars(calendar_id1, calendar_id2)):
            Operator.compare_calendars(calendar_id1, calendar_id2)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def remove_reminder(cls, reminder_id):
        if(RequestValidator.validate_remove_reminder(reminder_id)):
            Operator.remove_reminder(reminder_id)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def change_reminder(cls, reminder_id, new_time):
        if(RequestValidator.validate_change_reminder(reminder_id, new_time)):
            Operator.change_reminder(reminder_id, new_time)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def delete_profile(cls, profile_id):
        if(RequestValidator.validate_delete_profile(profile_id)):
            Operator.delete_profile(profile_id)
        else:
            raise Exception("Validation error occured")

    @classmethod
    def filter_by_dates(cls, calendar, start_date, end_date):
        if(RequestValidator.validate_dfilter_by_dates(calendar, start_date, end_date)):
            Operator.filter_by_dates(calendar, start_date, end_date)
        else:
            raise Exception("Validation error occured")

    def get_calendar():
        return calendar