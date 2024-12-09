# Author: Edwin Chavez
# Edit Reminder unit test
from InputController import InputController
from Reminder import Reminder
from Calendar import Calendar
import datetime
import pytest



@pytest.fixture(autouse=True)
def initializing():
    InputController.login("test","password")
    InputController.create_calendar("cal1")
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    InputController.add_event("testName",datetime.datetime(2024, 12, 8, 8,15),datetime.datetime(2024, 12, 12, 10,15),"A description")
    InputController.set_happening(InputController.get_calendar().retrieve_events()[0])
    InputController.create_reminder(datetime.datetime(2024, 12, 9, 9,00))
    yield
    InputController.delete_calendar()
    InputController.active_calendar = None
    InputController.active_happening = None
    InputController.active_reminder = None
    InputController.active_profile = None


def test_remove_reminder():
    assert InputController.remove_reminder() is True

def test_remove_reminder_with_none():
    InputController.remove_reminder()
    assert InputController.remove_reminder() is False