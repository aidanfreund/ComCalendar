from Profile import Profile
from DBFactory import FactoryProducer


class Operator:

    @classmethod
    def add_event(cls, event_id, name, start_time, end_time, calendar):
        pass

    @classmethod
    def edit_event(cls, event_id, new_name, new_description, start_time, end_time, calendar):
        pass

    @classmethod
    def delete_event(cls, event_id, calendar):
        pass

    @classmethod
    def create_calendar(cls, calendar_id, name):
        pass

    @classmethod
    def delete_calendar(cls, calendar_id):
        pass

    @classmethod
    def upload_calendar(cls, calendar):
        pass

    @classmethod
    def download_calendar(cls):
        pass

    @classmethod
    def aggregate_calendar(cls, calendar1, calendar2):
        pass

    @classmethod
    def create_reminder(cls, reminder_id, time):
        pass

    @classmethod
    def retrieve_calendar(cls, calendar_id):
        pass

    @classmethod
    def filter_calendar_by_events(cls, calendar, start_time, end_time):
        pass

    @classmethod
    def retrieve_event_information(cls, event_id, calendar):
        pass

    @classmethod
    def retrieve_task_information(cls, task_id, calendar):
        pass

    @classmethod
    def filter_calendar_by_tasks(cls, calendar, start_time, end_time):
        pass

    @classmethod
    def add_task(cls, task_id, description, due_date, calendar):
        pass

    @classmethod
    def remove_task(cls, task_id, calendar):
        pass

    @classmethod
    def edit_task(cls, task_id, new_name, new_description, due_date, calendar):
        pass

    @classmethod
    def copy_calendar(cls, calendar_id):
        pass

    @classmethod
    def compare_calendars(cls, calendar_id1, calendar_id2):
        pass

    @classmethod
    def remove_reminder(cls, reminder_id):
        pass

    @classmethod
    def change_reminder(cls, reminder_id, new_time):
        pass

    @classmethod
    def delete_profile(cls, profile_id):
        pass

    @classmethod
    def filter_by_dates(cls, calendar, start_date, end_date):
        pass

    @classmethod
    def validate_login(cls,username, password):
        pass

    @classmethod
    def create_profile(cls, username, password):
        pass
