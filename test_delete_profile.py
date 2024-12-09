#Author: DaShawn Pfeifer
import pytest
from datetime import datetime
from InputController import InputController

def test_add_task():
    InputController.create_profile('testuser50', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    task_name = 'Complete Report'
    task_description = 'Finish the quarterly report'
    task_due_date = datetime(2024, 12, 10, 10, 0)
    result = InputController.add_task(task_name, task_description, task_due_date)

    assert result is True
    tasks = InputController.get_calendar().retrieve_tasks()
    assert len(tasks) > 0
    last_task = tasks[-1]
    assert last_task.get_name() == task_name
    assert last_task.get_first_time() == task_due_date
    assert last_task.get_completed() is False

def test_add_task_missing_name():
    InputController.create_profile('testuser10', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    task_description = 'Finish the quarterly report'
    task_due_date = datetime(2024, 12, 10, 10, 0)

    result = InputController.add_task('', task_description, task_due_date)
    assert result is True

def test_add_multiple_tasks():
    InputController.create_profile('testuser', 'password')
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    task_name1 = 'Complete report'
    task_description1 = 'Finish the quarterly report'
    task_due_date1 = datetime(2024, 12, 10, 10, 0)
    result1 = InputController.add_task(task_name1, task_description1, task_due_date1)

    task_name2 = 'Prepare Presentation'
    task_description2 = 'Create slides for the meeting'
    task_due_date2 = datetime(2024, 12, 12, 9, 0)
    result2 = InputController.add_task(task_name2, task_description2, task_due_date2)

    assert result1 is True
    assert result2 is True

    tasks = InputController.get_calendar().retrieve_tasks()
    assert len(tasks) == 2
    assert tasks[0].get_name() == task_name1
    assert tasks[1].get_name() == task_name2
def test_add_task_no_calendar():
    InputController.create_profile('testuserrrr', 'password')
    task_name = 'Complete Report'
    task_description = 'Finish the quarterly report'
    task_due_date = datetime(2024, 12, 10, 10, 0)

    result = InputController.add_task(task_name, task_description, task_due_date)
    assert result is False

def test_add_task_same_due_date():
    InputController.create_profile("testuserr", "password")
    InputController.create_calendar('Work Calendar')
    InputController.set_calendar(InputController.get_profile().get_calendars()[0])
    task_name1 = 'Complete report'
    task_description1 = 'Finish the quarterly report'
    task_due_date1 = datetime(2024, 12, 10, 10, 0)
    result1 = InputController.add_task(task_name1, task_description1, task_due_date1)

    task_name2 = 'Prepare Presentation'
    task_description2 = 'Create slides for the meeting'
    task_due_date2 = datetime(2024, 12, 10, 10, 0)
    result2 = InputController.add_task(task_name2, task_description2, task_due_date2)

    assert result1 is True
    assert result2 is True

    tasks = InputController.get_calendar().retrieve_tasks()
    assert len(tasks) == 2
    assert tasks[0].get_name() == task_name1
    assert tasks[1].get_name() == task_name2

def test_delete_profile():
    InputController.create_profile('test_user', 'password123')
    assert InputController.get_profile() is not None
    result = InputController.delete_profile()
    assert result is True
    assert InputController.get_profile() is None

def test_delete_profile_no_existing_profile():
    result = InputController.delete_profile()
    assert result is False
    assert InputController.get_profile is None

def test_delete_profile_twice():
    InputController.create_profile('test_user', 'password123')
    assert InputController.get_profile() is not None
    result1 = InputController.delete_profile()
    assert result1 is True
    assert InputController.get_profile() is None

    result2 = InputController.delete_profile()
    assert result2 is False
