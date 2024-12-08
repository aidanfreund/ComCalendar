
import datetime
from Event import Event
from Task import Task
from RequestValidator import RequestValidator

def test_add_event():
    valid_name = "Meeting"
    valid_start_time = datetime.datetime(2024, 12, 8, 10, 0)
    valid_end_time = datetime.datetime(2024, 12, 8, 12, 0)
    valid_description = "Discuss project updates"
    
    assert RequestValidator.validate_add_event(valid_name, valid_start_time, valid_end_time, valid_description)

    invalid_name = "Meeting@!"
    invalid_description = "Project#details"
    assert not RequestValidator.validate_add_event(invalid_name, valid_start_time, valid_end_time, invalid_description)

def test_edit_event():
    valid_event = Event("Meeting", datetime.datetime(2024, 12, 8, 10, 0), datetime.datetime(2024, 12, 8, 12, 0), "Discuss updates")
    assert RequestValidator.validate_edit_event("Updated Meeting", datetime.datetime(2024, 12, 9, 10, 0), datetime.datetime(2024, 12, 9, 12, 0), "Changed description", valid_event)
    
    invalid_event = "NotAnEventObject"
    assert not RequestValidator.validate_edit_event("Meeting", datetime.datetime(2024, 12, 8, 10, 0), datetime.datetime(2024, 12, 8, 12, 0), "Discuss updates", invalid_event)

def test_delete_event():
    valid_event = Event("Meeting", datetime.datetime(2024, 12, 8, 10, 0), datetime.datetime(2024, 12, 8, 12, 0), "Discuss updates")
    assert RequestValidator.validate_delete_event(valid_event)

    invalid_event = "NotAnEventObject"
    assert not RequestValidator.validate_delete_event(invalid_event)

def test_create_calendar():
    valid_name = "Work Calendar"
    assert RequestValidator.validate_create_calendar(valid_name)

    invalid_name = "Work@Calendar!"
    assert not RequestValidator.validate_create_calendar(invalid_name)

def test_upload_calendar():
    valid_file_path = "/home/user/calendar.ics"
    valid_name = "My Calendar"
    assert RequestValidator.validate_upload_calendar(valid_file_path, valid_name)

    invalid_file_path = "invalid//path"
    assert not RequestValidator.validate_upload_calendar(invalid_file_path, valid_name)

def test_create_reminder():
    valid_time = datetime.datetime(2024, 12, 8, 9, 0)
    assert RequestValidator.validate_create_reminder(valid_time)

    invalid_time = "2024-12-08T09:00:00"
    assert not RequestValidator.validate_create_reminder(invalid_time)

def test_filter_calendar_by_dates():
    valid_start_date = datetime.datetime(2024, 12, 1)
    valid_end_date = datetime.datetime(2024, 12, 31)
    assert RequestValidator.validate_filter_calendar_by_dates(valid_start_date, valid_end_date)

    invalid_start_date = "2024-12-01"
    assert not RequestValidator.validate_filter_calendar_by_dates(invalid_start_date, valid_end_date)

def test_add_task():
    valid_name = "Complete report"
    valid_description = "Finish the year-end report"
    valid_due_date = datetime.datetime(2024, 12, 15)
    assert RequestValidator.validate_add_task(valid_name, valid_description, valid_due_date)

    invalid_due_date = "2024-12-15"
    assert not RequestValidator.validate_add_task(valid_name, valid_description, invalid_due_date)

def test_remove_task():
    valid_task = Task("Complete report", "Finish the report", datetime.datetime(2024, 12, 15))
    assert RequestValidator.validate_remove_task(valid_task)

    invalid_task = "NotATaskObject"
    assert not RequestValidator.validate_remove_task(invalid_task)

def test_edit_task():
    valid_task = Task("Complete report", "Finish the report", datetime.datetime(2024, 12, 15))
    assert RequestValidator.validate_edit_task("Updated Task", "Updated description", datetime.datetime(2024, 12, 20), False, valid_task)

    invalid_task = "NotATaskObject"
    assert not RequestValidator.validate_edit_task("Task", "Description", datetime.datetime(2024, 12, 20), False, invalid_task)

def test_edit_reminder():
    valid_time = datetime.datetime(2024, 12, 20, 15, 0)
    assert RequestValidator.validate_edit_reminder(valid_time)

    invalid_time = "2024-12-20T15:00:00"
    assert not RequestValidator.validate_edit_reminder(invalid_time)

def test_create_profile():
    valid_username = "User123"
    valid_password = "Pass123"
    assert RequestValidator.validate_create_profile(valid_username, valid_password)

    invalid_username = "User!@#"
    assert not RequestValidator.validate_create_profile(invalid_username, valid_password)

def test_validate_description():
    valid_description = "This is a valid description."
    assert RequestValidator._RequestValidator__validate_description(valid_description)

    invalid_description = "Invalid description!@#"
    assert not RequestValidator._RequestValidator__validate_description(invalid_description)

def test_validate_name():
    valid_name = "ValidName"
    assert RequestValidator._RequestValidator__validate_name(valid_name)

    invalid_name = "InvalidName@123"
    assert not RequestValidator._RequestValidator__validate_name(invalid_name)
