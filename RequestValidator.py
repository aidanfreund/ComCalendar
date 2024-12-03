from Operator import Operator
from Calendar import Calendar
from datetime import datetime


class RequestValidator:
    
    @classmethod
    def validate_login(cls, username, password):
        pass

    @classmethod
    def validate_add_event(cls, event_id, name, start_time, end_time, calendar):
        pass

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
    def validate_change_reminder(cls, reminder_id, new_time):
        pass

    @classmethod
    def validate_delete_profile(cls, user_id):
        pass
    
    @classmethod
    def validate_filter_by_dates(cls, calendar, start_time, end_time):
        pass