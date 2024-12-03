#may need to pip instal ICS

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
import datetime

from Calendar import Calendar as Com_Calendar
from Event import Event as Com_Event
from Task import Task as Com_Task

def read_ics_file(file_path, name:str):
    with open(file_path, 'r') as f:
        ics_content = f.read()
        
    # Parse the .ics file
    ics_calendar = ICS_Calendar(ics_content)

    # Create a new Calendar object
    calendar = Com_Calendar(name, [], [])

    # Iterate through events in the .ics file and add them to the Calendar
    for ics_event in ics_calendar.events:
        hap_id = ics_event.uid
        desc = ics_event.name
        start = ics_event.begin.datetime
        end = ics_event.end.datetime

        # Create an object and add it to the Calendar
        # ics only has events, if start and end time are the same, interperate the event as a task
        if start != end:
            happening = Com_Event(hap_id, desc, start, end)
            calendar.add_event(event)
        else:
            task = Com_Task(hap_id, desc, start)
            #assume tasks in past are completed
            if start < datetime.datetime.today():
                happening.flip_completed()
            calendar.add_task(task)

    return calendar

def write_ics_file(calendar, file_path):
    ics_calendar = ICS_Calendar()

    for event in calendar.RetrieveEvents():
        ics_event = ICS_Event()
        ics_event.uid = event.get_id()
        ics_event.name = event.get_name()
        ics_event.begin = event.get_first_time()
        ics_event.end = event.get_second_time()

        ics_calendar.events.add(ics_event)


    for task in calendar.RetrieveTasks():
        ics_event = ICS_Event()
        ics_event.uid = task.get_id()
        ics_event.name = task.get_name()
        ics_event.begin = task.get_first_time()
        ics_event.end = ics_event.begin

        ics_calendar.events.add(ics_event)

    with open(file_path, 'w') as f:
        f.writelines(ics_calendar.serialize_iter())

if __name__ == "__main__":
#test write
    # Create a Calendar object
    my_calendar = Com_Calendar("hello", [], [])

    # Add some events to the Calendar
    event1 = Com_Event("evnt1", datetime.datetime(2024, 12, 3, 10, 0), datetime.datetime(2024, 12, 3, 11, 0))
    event2 = Com_Event("evnt 2", datetime.datetime(2024, 12, 4, 12, 30), datetime.datetime(2024, 12, 4, 13, 30))
    task1 = Com_Task("task1",datetime.datetime(2024, 12, 5, 13, 30))
    task2 = Com_Task("gym",datetime.datetime(2024, 12, 5, 13, 30))

    my_calendar.AddEvent(event1)
    my_calendar.AddEvent(event2)
    my_calendar.AddTask(event2)
    my_calendar.AddTask(event2)

    # Write the events to an .ics file
    file_path = "C:\\Users\\aidan\\Desktop\\ComCalendar\\testmethods"
    write_ics_file(my_calendar, file_path)

#test read
    calendar = read_ics_file(file_path, "Test")
    for event in calendar.RetrieveEvents():
        print(event.get_name())
    for task in calendar.RetrieveTasks():
        print(task.get_name())
