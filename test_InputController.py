

from unittest.mock import MagicMock
from InputController import InputController
from Operator import Operator
from RequestValidator import RequestValidator
from Profile import Profile
from Calendar import Calendar
from Event import Event
from Task import Task
from Reminder import Reminder
import datetime


# Setup common test data
def setup_data():
    profile = Profile()
    calendar = Calendar("Test Calendar", profile)
    event = Event("Test Event", datetime.datetime(2024, 12, 8, 10, 0), datetime.datetime(2024, 12, 8, 12, 0), "Description")
    task = Task("Test Task", "Task description", datetime.datetime(2024, 12, 15))
    reminder = Reminder(datetime.datetime(2024, 12, 8, 9, 0))

    # Mock active objects in InputController
    InputController.active_profile = profile
    InputController.active_calendar = calendar
    InputController.active_happening = event
    InputController.active_reminder = reminder

    return profile, calendar, event, task, reminder


# Test add_event
def test_add_event(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'add_event', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_add_event', return_value=True)

    result = InputController.add_event("Meeting", datetime.datetime(2024, 12, 8, 10, 0), datetime.datetime(2024, 12, 8, 12, 0), "Discuss updates")
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test edit_event
def test_edit_event(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'edit_event', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_edit_event', return_value=True)

    result = InputController.edit_event("Updated Event", datetime.datetime(2024, 12, 9, 10, 0), datetime.datetime(2024, 12, 9, 12, 0), "Updated description")
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test delete_event
def test_delete_event(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'delete_event', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_delete_event', return_value=True)

    result = InputController.delete_event()
    assert result is True
    assert InputController.active_happening is None
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test create_calendar
def test_create_calendar(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'create_calendar', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_create_calendar', return_value=True)

    result = InputController.create_calendar("New Calendar")
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test delete_calendar
def test_delete_calendar(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'delete_calendar', return_value=True)

    result = InputController.delete_calendar()
    assert result is True
    assert InputController.active_calendar is None
    mock_operator.assert_called_once()


# Test upload_calendar
def test_upload_calendar(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'upload_calendar', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_upload_calendar', return_value=True)

    result = InputController.upload_calendar("/path/to/calendar.ics", "Uploaded Calendar")
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test create_reminder
def test_create_reminder(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'create_reminder', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_create_reminder', return_value=True)

    result = InputController.create_reminder(datetime.datetime(2024, 12, 8, 9, 0))
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test add_task
def test_add_task(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'add_task', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_add_task', return_value=True)

    result = InputController.add_task("New Task", "Task description", datetime.datetime(2024, 12, 15))
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test remove_task
def test_remove_task(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'remove_task', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_remove_task', return_value=True)

    result = InputController.remove_task()
    assert result is True
    assert InputController.active_happening is None
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test edit_task
def test_edit_task(mocker, setup_data):
    mock_operator = mocker.patch.object(Operator, 'edit_task', return_value=True)
    mock_validator = mocker.patch.object(RequestValidator, 'validate_edit_task', return_value=True)

    result = InputController.edit_task("Updated Task", "Updated description", datetime.datetime(2024, 12, 20), False)
    assert result is True
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()


# Test create_profile
def test_create_profile(mocker):
    mock_operator = mocker.patch.object(Operator, 'create_profile', return_value=Profile())
    mock_validator = mocker.patch.object(RequestValidator, 'validate_create_profile', return_value=True)

    result = InputController.create_profile("username", "password")
    assert result is True
    assert isinstance(InputController.active_profile, Profile)
    mock_validator.assert_called_once()
    mock_operator.assert_called_once()
