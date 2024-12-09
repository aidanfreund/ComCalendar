#Author: Justin Grage
#Edit event unit test

from InputController import InputController
from Calendar import Calendar
import datetime
import pytest


@pytest.fixture(autouse=True)
def setup():
    InputController.login("testuser","password")
    InputController.create_calendar("testCal")
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    InputController.add_event("testName",datetime.datetime(2024, 12, 8, 8,15),datetime.datetime(2024, 12, 12, 10,15),"A description")
    InputController.set_happening(InputController.get_calendar().retrieve_events()[0])
    yield 
    InputController.delete_calendar(InputController.active_calendar)
    InputController.active_calendar = None
    InputController.active_happening = None
    InputController.active_reminder = None
    InputController.active_profile = None


def test_edit_event_with_valid_input():
    assert InputController.edit_event("New name", datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new description") is True

def test_edit_event_with_none_for_a_parameter():
    assert InputController.edit_event(None, datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new description") is False

def test_edit_event_with_invalid_name():
    assert InputController.edit_event("[][da*123%]", datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new description") is False

def test_edit_event_with_invalid_description():
    assert InputController.edit_event(None, datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new descriptiona&*)!@#") is False

def test_edit_event_with_wrong_type():
    assert InputController.edit_event(None, datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new descriptiona&*)!@#") is False

def test_edit_event_with_wrong_happening_type():
    InputController.add_task("testTask","A description",datetime.datetime(2024, 12, 12, 10,15))
    InputController.set_happening(Calendar(InputController.get_calendar()).retrieve_tasks()[0])
    assert InputController.edit_event(None, datetime.datetime(2024, 10, 8, 8,15),datetime.datetime(2024, 11, 12, 10,15), "A new descriptiona&*)!@#") is False

