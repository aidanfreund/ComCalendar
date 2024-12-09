# Author: Aidan Freund
# tests the "add event" use case
import pytest
from datetime import datetime
from InputController import InputController


def test_add_event():
    InputController.create_profile('testuser0', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    event_name = 'Complete Report'
    event_description = 'Finish the quarterly report'
    event_start_time = datetime(2024, 12, 10, 10, 0)
    event_end_time = datetime(2024, 12, 10, 11, 0)  # Second time for the event
    result = InputController.add_event(event_name, event_start_time, event_end_time, event_description)

    assert result is True
    events = InputController.get_calendar().retrieve_events()
    assert len(events) > 0
    last_event = events[-1]
    assert last_event.get_name() == event_name
    assert last_event.get_first_time() == event_start_time
    assert last_event.get_second_time() == event_end_time
    InputController.delete_profile()

def test_add_event_missing_name():
    InputController.create_profile('testuser1', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    event_description = 'Finish the quarterly report'
    event_start_time = datetime(2024, 12, 10, 10, 0)
    event_end_time = datetime(2024, 12, 10, 11, 0)  

    result = InputController.add_event('', event_start_time, event_end_time, event_description)
    assert result is True
    InputController.delete_profile()

def test_add_multiple_events():
    InputController.create_profile('testuser3', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    event_name1 = 'Complete report'
    event_description1 = 'Finish the quarterly report'
    event_start_time1 = datetime(2024, 12, 10, 10, 0)
    event_end_time1 = datetime(2024, 12, 10, 11, 0)
    result1 = InputController.add_event(event_name1, event_start_time1, event_end_time1, event_description1)

    event_name2 = 'Prepare Presentation'
    event_description2 = 'Create slides for the meeting'
    event_start_time2 = datetime(2024, 12, 12, 9, 0)
    event_end_time2 = datetime(2024, 12, 12, 10, 0)  # Second time for the event
    result2 = InputController.add_event(event_name2, event_start_time2, event_end_time2, event_description2)

    assert result1 is True
    assert result2 is True

    events = InputController.get_calendar().retrieve_events()
    assert len(events) == 2
    assert events[0].get_name() == event_name1
    assert events[0].get_first_time() == event_start_time1
    assert events[0].get_second_time() == event_end_time1
    assert events[1].get_name() == event_name2
    assert events[1].get_first_time() == event_start_time2
    assert events[1].get_second_time() == event_end_time2
    InputController.delete_profile()

def test_add_event_same_times():
    InputController.create_profile('testuser4', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    event_name1 = 'Complete report'
    event_description1 = 'Finish the quarterly report'
    event_start_time1 = datetime(2024, 12, 10, 10, 0)
    event_end_time1 = datetime(2024, 12, 10, 11, 0) 
    result1 = InputController.add_event(event_name1, event_start_time1, event_end_time1, event_description1)

    event_name2 = 'Prepare Presentation'
    event_description2 = 'Create slides for the meeting'
    event_start_time2 = datetime(2024, 12, 10, 10, 0)
    event_end_time2 = datetime(2024, 12, 10, 11, 0)  
    result2 = InputController.add_event(event_name2, event_start_time2, event_end_time2, event_description2)

    assert result1 is True
    assert result2 is True

    events = InputController.get_calendar().retrieve_events()
    assert len(events) == 2
    assert events[0].get_name() == event_name1
    assert events[0].get_first_time() == event_start_time1
    assert events[0].get_second_time() == event_end_time1
    assert events[1].get_name() == event_name2
    assert events[1].get_first_time() == event_start_time2
    assert events[1].get_second_time() == event_end_time2
    InputController.delete_profile()

