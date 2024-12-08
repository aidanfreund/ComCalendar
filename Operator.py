#operator.py
#Class to handle operation requests
from Profile import Profile
from DBProfile import DBProfile,MySQLProfile
from Calendar import Calendar
from DBFactory import DatabaseFactory, FactoryProducer
from DBConnection import DatabaseConnection
from datetime import timezone, datetime

from Profile import Profile
from Calendar import Calendar
from Event import Event
from Task import Task
from Reminder import Reminder
from Happening import Happening

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
import os

class Operator:

    factory:DatabaseFactory = FactoryProducer("Profile").factory
    db_profile:DBProfile = factory.DB_profile

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, description, calendar_obj):
        new_event_id = cls.db_profile.add_event(description,start_time,end_time,name,calendar_obj)
        if new_event_id is not -1:
            calendar_obj.add_event(new_event_id,name,start_time,end_time,description)
            return True
        else:
            return False
  
    # Edits event, returns true if successful
    @classmethod
    def edit_event(cls, name:str, start_time:datetime, end_time:datetime, event_obj:Event, desc:str):
        #update on machine
        event_obj.set_name(name)
        event_obj.set_first_time(start_time)
        event_obj.set_second_time(end_time)
        event_obj.set_description(desc)
        #attempt update in db
        return cls.db_profile.change_event(event_obj)
    
    # Deletes event from calendar, returns true if successful
    @classmethod
    def delete_event(cls, event_obj:Event, calendar_obj:Calendar):
        #delete from db
        db = cls.db_profile.delete_event(event_obj)
        #delete from machine
        mach = calendar_obj.delete_event(event_obj.get_id())

        return (db and mach)
    
    # Creates new calendar with name, returns true if successful
    @classmethod
    def create_calendar(cls, name, profile_obj:Profile):
        #check amount of calendars assosciated with profile, ensure its less than 6(the max)
        if len(profile_obj.get_calendars())<6:
            #create in db
            id = cls.db_profile.add_calendar(name, profile_obj)
            #create on machine
            return profile_obj.create_new_calendar(id, name)

        else:
            print("Profile may only have 6 calendars, delete one and try again")
            return False
    
    # Deletes calendar 
    @classmethod
    def delete_calendar(cls, calendar_obj:Calendar, profile_obj:Profile):
        #delete from db
        db = cls.db_profile.delete_calendar(calendar_obj)
        #delete on machine
        mach = profile_obj.delete_calendar(calendar_obj)
        return (mach and db)

      # Processes .ics file string and returns a boolean indicating its success
    @classmethod
    def upload_calendar(cls, file_path:str,  name:str, profile_obj:Profile):
        """reads an ICS file to create a calendar obj.  provided a file path to read from, 
        a name for the calendar, and the profile obj to be added to.
        will return calendar object. assumes user is in UTC time zone 
        (in order to reduce required downloads)"""
        #first ensure profile has no more than 5 calendars already
        if len(profile_obj.get_calendars())<6:
            #create in db
            id = cls.db_profile.add_calendar(name, profile_obj)
            #create on machine
            calendar_made = profile_obj.create_new_calendar(id, name)
        else:
            print("Profile may only have 6 calendars, delete one and try again")
            return False
        
        #validate file
        #open path and read
        if not os.path.exists(file_path):
            print(f"Error: File path '{file_path}' does not exist.")
            return False
        if not file_path.endswith(".ics"):
            print(f"Error: File path '{file_path}' is not an ICS file.")
            return False
        with open(file_path, 'r') as f:
            ics_content = f.read()
        ics_calendar = ICS_Calendar(ics_content)

        if calendar_made:
            #get cal obj
            cals = profile_obj.get_calendars()
            for cal in cals:
                if cal.get_calendar_id() == id:
                    calendar = cal
                    break
            #find current time
            today = datetime.now()
            today = today.replace(tzinfo=None)
            # Iterate through events in the .ics file and add them to the Calendar
            for ics_event in ics_calendar.events:
                name = ics_event.name
                start = ics_event.begin
                end = ics_event.end
                desc = ics_event.description

                start = start.naive
                end = end.naive
                #Create an object and add it to the Calendar
                #ics only has events, if start and end time are the same, interperate the event as a task    
                if start != end:
                    id = cls.db_profile.add_event(desc, start, end, name, calendar)
                    calendar.add_event(id, name, start, end, desc)
                else:
                    task = Task(id, name, start,desc)
                    #assume tasks in past are completed
                    if start < today:
                        task.set_completed(False)
                    calendar.add_task(id,start,name,desc)

            return True
        else:
            return False
            
    #downloads desired calendar to the desktop with the name of the calendar as an ICS file
    #Returns the file string
    @classmethod
    def download_calendar(cls, calendar:Calendar):
        """Simply takes a calendar, and writes the file in ics format, 
        it will save to the desktop with the calendar name"""

       # Set default path to user Desktop
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        calendar_name = calendar.get_calendar_name()
        
        # Sanitize calendar name
        calendar_name = ''.join(c for c in calendar_name if c.isalnum() or c in (' ', '_', '-'))

        file_path = os.path.join(desktop_path, f"{calendar_name}.ics")
        
        # Ensure the directory exists
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory) 
        
        # Initialize ICS calendar object
        ics_calendar = ICS_Calendar()

        # Add each event and task to the ICS calendar
        for event in calendar.retrieve_events():
            ics_event = ICS_Event()
            ics_event.uid = str(event.get_id())
            ics_event.name = event.get_name()
            ics_event.begin = event.get_first_time()
            ics_event.end = event.get_second_time()
            ics_event.description = event.get_description()
            ics_calendar.events.add(ics_event)

        for task in calendar.retrieve_tasks():
            ics_event = ICS_Event()
            ics_event.uid = str(task.get_id())
            ics_event.name = task.get_name()
            ics_event.begin = task.get_first_time()
            ics_event.end = ics_event.begin
            ics_event.description = task.get_description() 
            ics_calendar.events.add(ics_event)

        # Write the ICS file to the specified file path
        with open(file_path, 'w') as f:
            f.writelines(ics_calendar.serialize_iter())

        return f"{file_path}"

    #creates an identical calendar with the same name+ " copy", takes in a calendar and 
    @classmethod
    def copy_calendar(cls, calendar_obj:Calendar, profile_obj:Profile):
        #check amount of calendars assosciated with profile, ensure its less than 6(the max)
        if len(profile_obj.get_calendars())<6:
            name = calendar_obj.get_calendar_name()+" copy"
            #create in db
            id = cls.db_profile.add_calendar(name, profile_obj)
            #create on machine

            events = calendar_obj.retrieve_events()
            tasks = calendar_obj.retrieve_tasks()
            copy_calendar = Calendar(id, name, events, tasks)

            cal_created = profile_obj.create_new_calendar(id, name, events, tasks)
            if cal_created:
                #update calendar in db
                cls.db_profile.change_calendar(copy_calendar, profile_obj)
            return cal_created
        else:
            print("Profile may only have 6 calendars, delete one and try again")
            return False
        

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod
    def compare_calendars(cls, calendar1:Calendar, calendar2:Calendar):
        
        def find_free_slots(events):
            # Find free slots between events
            free_slots = []
            current_time = datetime.now()
            for i in range(len(events) - 1):
                end_time = events[i].get_second_time()
                next_start_time = events[i + 1].get_first_time()
                if end_time < next_start_time:
                    free_slots.append((end_time, next_start_time))
            # Add free slot from now until the first event, if applicable
            if events:
                first_event_start = events[0].get_first_time()
                if current_time < first_event_start:
                    free_slots.insert(0, (current_time, first_event_start))
            return free_slots

        events1 = calendar1.retrieve_events()
        events2 = calendar2.retrieve_events()
        
        free_slots1 = find_free_slots(events1)
        free_slots2 = find_free_slots(events2)

        shared_freetime = ""
        slots, i, j = 0, 0, 0
        while i < len(free_slots1) and j < len(free_slots2) and slots < 5:
            start1, end1 = free_slots1[i]
            start2, end2 = free_slots2[j]
            # Find the overlapping time slot
            start_shared = max(start1, start2)
            end_shared = min(end1, end2)
            if start_shared < end_shared:
                slots += 1
                shared_freetime += f"slot {slots}: {start_shared} -> {end_shared}\n"
                
            # Move to the next free slot
            if end1 < end2:
                i += 1
            else:
                j += 1

        return shared_freetime
    
    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def aggregate_calendar(cls,name:str, calendar1:Calendar, calendar2:Calendar, profile_obj:Profile):
        
        if len(profile_obj.get_calendars())<6:

            #create new blank calendar in db
            id = cls.db_profile.add_calendar(name, profile_obj)

            #create full calendar on machine
            events = calendar1.retrieve_events() + calendar2.retrieve_events()
            tasks = calendar1.retrieve_tasks() + calendar2.retrieve_tasks()
            agg_calendar = Calendar(id, name, events, tasks)

            cal_created = profile_obj.create_new_calendar(id, name, events, tasks)
            if cal_created:
                #update calendar in db
                cls.db_profile.change_calendar(agg_calendar, profile_obj)
            return cal_created
        else:
            print("Profile may only have 6 calendars, delete one and try again")
            return False

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, time:datetime, happ_obj:Happening):
        #add in db
        id = cls.db_profile.add_reminder(time, happ_obj)
        #add in machine
        return happ_obj.create_reminder(id, time)

     # Filters calendar by events in the future, returns a fstring of events that end after now
    @classmethod
    def filter_calendar_by_events(cls, calendar_obj: Calendar):
        events = calendar_obj.retrieve_events()
        future_events = f"Calendar {calendar_obj.get_calendar_name()} Events:\n"
        i = 0
        for event in events:
            if event.get_second_time() > datetime.now():
                future_events += f"{i+1}. Name: {event.get_name()} Start: {event.get_first_time()}, End: {event.get_second_time()} Description: {event.get_description()}\n"
                i += 1
        return future_events


    # Filters calendar by tasks, returns a string of tasks to be completed in the future
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj: Calendar):
        tasks = calendar_obj.retrieve_tasks()
        future_tasks = f"Calendar {calendar_obj.get_calendar_name()} Tasks:\n"
        i = 0
        for task in tasks:
            if task.get_first_time() > datetime.now():
                future_tasks += f"{i+1}. Name: {task.get_name()} Start: {task.get_first_time()} Completion Status: {task.get_completed()} Description: {task.get_description()}\n"
                i += 1
        return future_tasks
     
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj:Calendar, start_date, end_date):
        filtered_events = [event for event in calendar_obj.retrieve_events() if start_date<= event.get_first_time() <= end_date]
        return Calendar(calendar_obj.get_calendar_id(), calendar_obj.get_calendar_name(), filtered_events, calendar_obj.retrieve_tasks())


    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, name:str, description:str, time:datetime, calendar_obj:Calendar):
        #add in db
        id = cls.db_profile.add_task(description,time,name, calendar_obj)
        #add in machine
        return calendar_obj.add_task(id, time, name, description)
        
        return True
    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls, task_obj:Task, calendar_obj:Calendar):
        #delete from db
        db = cls.db_profile.delete_task(task_obj)
        #delete from machine
        mach = calendar_obj.delete_task(task_obj.get_id())
        return (db and mach)

    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls, name:str, desc:str, time:datetime, completion:bool, task_obj:Task):
        #update on machine
        task_obj.set_name(name)
        task_obj.set_first_time(time)
        task_obj.set_description(desc)
        task_obj.set_completed(completion)
        #attempt update in db
        return cls.db_profile.change_task(task_obj)
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls, reminder_obj:Reminder, happ_obj:Happening):
        #delete from db
        db = cls.db_profile.delete_reminder(reminder_obj)
        #delete from machine
        happ_obj.set_reminder(None)
        return db 

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, reminder_obj:Reminder, new_time:datetime):
        #update on machine
        reminder_obj.set_time(new_time)
        #attempt update in db
        return cls.db_profile.change_reminder(reminder_obj)
        
    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls, profile_obj: Profile):
        profile_id = profile_obj.get_profile_id()
        if cls.db_profile.delete_profile(profile_id):
            for calendar in profile_obj.get_calendars():
                cls.db_profile.delete_calendar(calendar)
            return True
        else:
            return False

   
    #Logs in to profile using username and password
    #Returns profile obj if a match exists
    @classmethod
    def attempt_login(cls, username: str, password: str):
        profile = cls.db_profile.read_profile(username, password)
        if profile != None:
            calendars = cls.db_profile.read_calendars(profile)
            for cal in calendars:
                events = cls.db_profile.read_events(cal)
                for event in events:
                    event.set_reminder(cls.db_profile.read_reminder(event))
                tasks = cls.db_profile.read_tasks(cal)
                for task in tasks:
                    task.set_reminder(cls.db_profile.read_reminder(task))
                profile.create_new_calendar(cal.get_calendar_id(), cal.get_calendar_name(), events, tasks)

            return profile
        else:
            print("Invalid username or password.")
            return None

    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username: str, password: str):
        if not cls.db_profile.check_username_unique(username):
            return False
        profile_id = cls.db_profile.add_profile(username, password)
        if profile_id == -1:
            return None
        new_profile = Profile(username, profile_id, [])
        return new_profile      

