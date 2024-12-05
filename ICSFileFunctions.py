#may need to pip install ics

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
from datetime import timezone, datetime
import os

from Calendar import Calendar as Com_Calendar
from Event import Event as Com_Event
from Task import Task as Com_Task


def read_ics_file(file_path, name:str):
    """reads an ICS file to create a calendar obj.  provided a file path to read from, and a name for the calendar.
   will return calendar object (will need ID assigned later). assumes user is in UTC time zone 
   (in order to reduce required downloads)"""
    with open(file_path, 'r') as f:
        ics_content = f.read()
        
    ics_calendar = ICS_Calendar(ics_content)

    # Create a new Calendar object
    calendar = Com_Calendar(-1, name, [], [])
    #find current time, and convert to utc
    today = datetime.now()
    today = today.replace(tzinfo=timezone.utc)
    # Iterate through events in the .ics file and add them to the Calendar
    for ics_event in ics_calendar.events:
        hap_id = ics_event.uid
        desc = ics_event.name
        start = ics_event.begin
        end = ics_event.end

        # Create an object and add it to the Calendar
        # ics only has events, if start and end time are the same, interperate the event as a task
        if start != end:
            event = Com_Event(hap_id, desc, start, end)
            calendar.add_event(event)
        else:
            task = Com_Task(hap_id, desc, start)
            #assume tasks in past are completed
            if start < today:
                task.flip_completed()
            calendar.add_task(task)

    return calendar

def write_ics_file(calendar, file_path = ""):
    """Simply takes a calendar and a file path  to write to, and writes the file in ics format
       if no path is provided it will save to the desktop with the calendar name"""
    #set default path to user desktop
    if file_path == "":
        file_path = os.path.join(os.path.expanduser("~"), "Desktop") 
        file_path = os.path.join(file_path, calendar.get_calendar_name())    
    #default as ics file type
    if not file_path.endswith(".ics"): 
        file_path += ".ics" 

    ics_calendar = ICS_Calendar()

    #add each event and task to file, must save a task as an event with same start and end time
    for event in calendar.retrieve_events():
        print(event)
        ics_event = ICS_Event()
        ics_event.uid = str(event.get_id())
        ics_event.name = event.get_name()
        ics_event.begin = event.get_first_time()
        ics_event.end = event.get_second_time()

        ics_calendar.events.add(ics_event)

    for task in calendar.retrieve_tasks():
        ics_event = ICS_Event()
        ics_event.uid = str(task.get_id())  
        ics_event.name = task.get_name()
        ics_event.begin = task.get_first_time()
        ics_event.end = ics_event.begin

        ics_calendar.events.add(ics_event)

    with open(file_path, 'w') as f:
        f.writelines(ics_calendar.serialize_iter())