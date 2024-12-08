from Task import Task
from Event import Event
from Calendar import Calendar
from datetime import datetime

def main():
    calendar = Calendar(1, "Cal1",[], [])

    task1 = datetime(2024, 12, 7, 9, 0)
    task2 = datetime(2024, 12, 7, 10, 0)
    event1 = datetime(2024, 12, 7, 11, 0)
    event2 = datetime(2024, 12, 7, 13, 0)
    event3 = datetime(2024, 12, 5, 9, 0)
    event4 = datetime(2024, 12, 5, 10, 0)

    calendar.add_task(1, task1, "Task 1", "This is the description for the first task")
    calendar.add_task(2, task2, "Task 2", "Description for the second task")
    calendar.add_event(1, "Event 1", event1, event2, "Event 1 description")
    calendar.add_event(2, "Event 2", event3, event4, "Event 2 description")
    

    # print("Task in order:")
    # for task in calendar._tasks:
    #     print(task)

    # print("\nEvents in order:")
    # for event in calendar._events:
    #     print(event)
    print(calendar)
if __name__ == "__main__":
    main()