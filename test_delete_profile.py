#Author DaShawn
import pytest
from datetime import datetime
from InputController import InputController


def test_delete_profile():
    InputController.create_profile('testuser', 'password123')
    assert InputController.get_profile() is not None
    result = InputController.delete_profile()
    assert result is True
    assert InputController.get_profile() is None

def test_deleter_profile_no_existing_profile():
    result = InputController.delete_profile()
    assert result is False
    assert InputController.get_profile() is None

def test_delete_profile_twice():
    InputController.create_profile('testuser', 'password123')
    assert InputController.get_profile() is not None
    result1 = InputController.delete_profile()
    assert result1 is True
    assert InputController.get_profile() is None

    result2 = InputController.delete_profile()
    assert result2 is False
def test_delete_profile_with_data():
    InputController.create_profile('testuser', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    InputController.add_task('Complete Report', 'Finish the quarterly report', datetime(2024, 12, 10, 10, 0))

    assert len(InputController.get_profile().get_calendars())>0
    assert len(InputController.get_calendar().retrieve_tasks())>0

    result = InputController.delete_profile()
    assert result is True
    assert InputController.get_profile() is None
    assert len(InputController.get_profile().get_calendars()) == 0