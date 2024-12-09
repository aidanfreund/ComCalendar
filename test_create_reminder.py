#Author: Justin Grage
#Create reminder unit test

from InputController import InputController
from Reminder import Reminder
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
    

def test_create_reminder_with_valid_time():
    assert InputController.create_reminder(datetime.datetime(2024, 12, 8, 10,15)) is True

def test_create_reminder_with_none():
    assert InputController.create_reminder(None) is False