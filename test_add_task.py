import pytest
from datetime import datetime
from InputController import InputController

def test_add_task():
    InputController.login('create', 'profile')
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