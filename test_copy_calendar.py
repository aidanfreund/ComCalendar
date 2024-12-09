# Author: Aidan Freund
# tests the "copy calendar" use case
import pytest
from datetime import datetime, timedelta
from InputController import InputController

def test_copy_calendar_success():
    InputController.create_profile('testuser5', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    
    # Add events to the original calendar
    event_name = 'Meeting'
    event_description = 'Discuss project'
    event_start_time = datetime(2024, 12, 11, 9, 0)
    event_end_time = datetime(2024, 12, 11, 10, 0)
    InputController.add_event(event_name, event_start_time, event_end_time, event_description)
    
    # Add tasks to the original calendar
    task_name = 'Complete Report'
    task_description = 'Finish the quarterly report'
    task_due_date = datetime(2024, 12, 12, 10, 0)
    InputController.add_task(task_name, task_description, task_due_date)
    
    # Copy the calendar
    result = InputController.copy_calendar()
    
    assert result is True
    calendars = InputController.get_profile().get_calendars()
    
    assert len(calendars) == 2
    original_calendar = calendars[0]
    copied_calendar = calendars[1]
    
    # Verify the copied calendar's name
    assert copied_calendar.get_calendar_name() == original_calendar.get_calendar_name() + " copy"
    
    # Verify the events are copied
    original_events = original_calendar.retrieve_events()
    copied_events = copied_calendar.retrieve_events()
    
    assert len(original_events) == len(copied_events)
    
    for original_event, copied_event in zip(original_events, copied_events):
        assert original_event.get_name() == copied_event.get_name()
        assert original_event.get_first_time() == copied_event.get_first_time()
        assert original_event.get_second_time() == copied_event.get_second_time()
        assert original_event.get_description() == copied_event.get_description()
    
    # Verify the tasks are copied
    original_tasks = original_calendar.retrieve_tasks()
    copied_tasks = copied_calendar.retrieve_tasks()
    
    assert len(original_tasks) == len(copied_tasks)
    
    for original_task, copied_task in zip(original_tasks, copied_tasks):
        assert original_task.get_name() == copied_task.get_name()
        assert original_task.get_first_time() == copied_task.get_first_time()
        assert original_task.get_description() == copied_task.get_description()
    
    InputController.delete_profile()

def test_copy_calendar_no_events_or_tasks():
    InputController.create_profile('testuser6', 'password')
    InputController.create_calendar('Personal Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    
    # Copy the calendar
    result = InputController.copy_calendar()
    
    assert result is True
    calendars = InputController.get_profile().get_calendars()
    
    assert len(calendars) == 2
    original_calendar = calendars[0]
    copied_calendar = calendars[1]
    
    # Verify the copied calendar's name
    assert copied_calendar.get_calendar_name() == original_calendar.get_calendar_name() + " copy"
    
    # Verify no events or tasks are copied
    original_events = original_calendar.retrieve_events()
    copied_events = copied_calendar.retrieve_events()
    original_tasks = original_calendar.retrieve_tasks()
    copied_tasks = copied_calendar.retrieve_tasks()
    
    assert len(original_events) == 0
    assert len(copied_events) == 0
    assert len(original_tasks) == 0
    assert len(copied_tasks) == 0
    
    InputController.delete_profile()

