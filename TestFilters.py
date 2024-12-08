from Task import Task
from Event import Event
from Calendar import Calendar
from datetime import datetime
from Operator import Operator


class TestOperator:

    def test_filter_by_event():
        event1 = Event(1, "Event 1", datetime(2024, 12, 7, 9, 0), datetime(2024, 12, 7, 10, 0), "First event")
        event2 = Event(2, "Event 3", datetime(2024, 12, 7, 11, 0), datetime(2024, 12, 7, 12, 0), "Second event")

        calendar = Calendar(1, "My Calendar", [event1,event2], [])
        filtered_calendar = Operator.filter_calendar_by_events(calendar, event1)

        print("Filtered by Event:")
        for event in filtered_calendar.retrieve_events():
            print(f"Event: {event.get_name()}, Start Time: {event.get_first_time()}, End Time: {event.get_second_time()}")
    def test_filter_by_task():
        task1 = Task(1, "Task 1", datetime(2024, 12, 7, 9, 0), "Task for event 1")
        task2 = Task(2, "Task 2", datetime(2024, 12, 7, 11, 0), "Task for event 2")
        event1 = Event(1, "Event 1", datetime(2024, 12, 7, 9, 0), datetime(2024, 12, 7, 10, 0), "First event")
        event2 = Event(2, "Event 2", datetime(2024, 12, 7, 11, 0), datetime(2024, 12, 7, 12, 0), "Second event")

        event1.set_task(task1)
        event2.set_task(task2)

        calendar = Calendar(1, "My Calendar", [event1, event2], [task1, task2])
        filtered_calendar = Operator.filter_calendar_by_task(calendar, task1)

        print("Filtered by Task:")
        for event in filtered_calendar.retrieve_events():
            print(f"Event: {event.get_name()}, Task: {event.get_task().get_name()}, Start Time: {event.get_first_time()}")
    def test_filter_by_dates():
        event1 = Event(1, "Event 1", datetime(2024, 12, 7, 9, 0), datetime(2024, 12, 7, 10, 0), "First event")
        event2 = Event(3, "Event 3", datetime(2024, 12, 8, 9, 0), datetime(2024, 12, 8,10,0), "Third event")

        calendar = Calendar(1, "My Calendar", [event1, event2], [])
        start_date = datetime(2024, 12, 7, 0, 0)
        end_date = datetime(2024, 12, 7, 23, 59)
        filtered_calendar = Operator.filter_calendar_by_dates(calendar, start_date, end_date)
        print("Filtered by Date Range:")
        for event in filtered_calendar.retrieve_events():
            print(f"Event: {event.get_name()}, Start Time: {event.get_first_time()}, End Time: {event.get_second_time()}")

if __name__ == "__main__":
    test_operator = TestOperator()
    test_operator.test_filter_by_event()
    print()
    test_operator.test_filter_by_task()
    print()
    test_operator.test_filter_by_event()