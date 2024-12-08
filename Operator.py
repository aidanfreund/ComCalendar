#operator.py
#Class to handle operation requests

from Profile import Profile

from DBProfile import DBProfile
from Calendar import Calendar
from DBFactory import DatabaseFactory, FactoryProducer
from DBConnection import DatabaseConnection
from datetime import timezone, datetime

from Profile import Profile
from Calendar import Calendar
from Event import Event
from Task import Task
from Reminder import Reminder

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
import os

class Operator:

    factory:DatabaseFactory = FactoryProducer("Profile")
    db_profile:DBProfile = factory.DB_profile

    # Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, description, calendar_obj):
        new_event_id = cls.db_profile.add_event(description,start_time,end_time,name,calendar_obj)
        if new_event_id is not -1:
            calendar_obj.add_event(Event(new_event_id,name,start_time,end_time,description))
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
        #
        cls.db_profile.delete_calendar(calendar_obj)
        #remove from profile array to delete
        profile_obj.delete_calendar(calendar_obj)
        pass
    
    @classmethod
    def create_profile(cls, username: str, password: str):
        profile_id = cls.db_profile.add_profilr(username, password)
        if profile_id == -1:
            return None
        new_profile = Profile(username, profile_id, [])
        return new_profile
    @classmethod
    def delete_profile(cls, profile_obj: Profile):
        profile_id = profile_obj.get_profile_id()
        if cls.db_profile.delete_profile(profile_id):
            for calendar in profile_obj.get_calendars():
                cls.db_profile.delete_calendar(calendar)
            return True
        else:
            return False
    @classmethod
    def login(cls, username: str, password: str):
        profile_id = cls.db_profile.verify_user_credentials(username, password)
        if profile_id != -1:
            profile_obj = cls.get_profile_by_id(profile_id)
            return profile_obj
        else:
            print("Invalid username or password.")
            return None
    @classmethod
    def filter_calendar_by_events(cls, calendar_obj: Calendar, event_filter):
        filtered_events = [event for event in calendar_obj.retrieve_events() if event == event_filter]
        return Calendar(calendar_obj.get_calendar_id(), calendar_obj.get_calendar_name(), filtered_events, calendar_obj.retrieve_tasks())
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj: Calendar, task_filter):
        filtered_tasks = [task for task in calendar_obj.retrieve_tasks() if task == task_filter]
        return Calendar(calendar_obj.get_calendar_id(), calendar_obj.get_calendar_name(), calendar_obj.retrieve_events(), filtered_tasks)
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj:Calendar, start_date, end_date):
        filtered_events = [event for event in calendar_obj.retrieve_events() if start_date<= event.get_first_time() <= end_date]
        return Calendar(calendar_obj.get_calendar_id(), calendar_obj.get_calendar_name(), filtered_events, calendar_obj.retrieve_tasks())
    # Processes .ics file string and returns a boolean indicating its success
    @classmethod
    def upload_calendar(cls, name:str, file_path:str, profile_obj:Profile):
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
            #find current time, and convert to utc
            calendar = Calendar(id, "temp", [], [])
            today = datetime.now()
            today = today.replace(tzinfo=timezone.utc)
            # Iterate through events in the .ics file and add them to the Calendar
            for ics_event in ics_calendar.events:
                desc = ics_event.name
                start = ics_event.begin
                end = ics_event.end

                # Create an object and add it to the Calendar
                # ics only has events, if start and end time are the same, interperate the event as a task
                
                # if start != end:
                #     id = cls.db_profile.add_event(desc, start, end, name, cls.db_profile.))
                #     calendar.add_event(id, )
                # else:
                #     task = Task(hap_id, desc, start)
                #     #assume tasks in past are completed
                #     if start < today:
                #         task.set_completed(False)
                    #calendar.add_task(task)

                #update db calendar

            return True
        else:
            return False
    
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls, calendar_obj):
        pass

     # Copies a calendar and adds it to profile, returns true if successful
    @classmethod
    def copy_calendar(cls, calendar_obj, profile_obj):
        pass

    # Compares calendars in a given time frame, returns string of *(conflicts or free space?)
    @classmethod

    def compare_calendars(cls, calendar_id1, calendar_id2):

  
        # cals = Profile.get_calendars()

        # for calendar in cals:
        #     if calendar.get_id() ==calendar_id1:
        #         events += calendar.get_events()
        #     elif calendar.get_id() ==calendar_id2:
        #         events += calendar.get_events()
        # min_time = datetime.now()
        # max_time = 0
        # freetime = ""
        # for event in events:
        #     first = event.get_first_time()
            
        return 
    
    # Combines calendars, returns a new calendar with combined objects
    @classmethod
    def aggregate_calendar(cls,name:str, calendar_id1:int, calendar_id2:int):
#work required
#i will come back to
        cls.db_profile.add_calendar(name, cls.db_profile.read_profile())

        new_id = -1
        events= []
        tasks = []
        # cals = Profile.get_calendars()
        
        # #find calendars and add their happenings to new calendar:
        # for calendar in cals:
        #     if calendar.get_id() ==calendar_id1:
        #         events += calendar.get_events()
        #         tasks += calendar.get_tasks()
        #     elif calendar.get_id() ==calendar_id2:
        #         events += calendar.get_events()
        #         tasks += calendar.get_tasks()
        agg_calendar = Calendar(new_id, name, events, tasks)

        return agg_calendar

    # Adds reminder to happening obj, returns true if successful
    @classmethod
    def create_reminder(cls, start_time, happ_obj):
        pass

     # Filters calendar by events, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_events(cls, calendar_obj):
        pass


    # Filters calendar by tasks, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj):
        pass
    
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        pass

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, name, description, due_date, calendar_obj):
        pass

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls, task_obj, calendar_obj):
        pass

    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls,name, description, due_date, is_completed, task_obj):
        pass
    
    # Removes reminder, returns true if successful
    @classmethod
    def remove_reminder(cls, reminder_obj, happ_obj):
        pass

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, reminder_obj, new_time):
        pass

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls, profile_obj):
        pass

   
    #Logs in to profile using username and password
    #Returns profile obj if a match exists
    @classmethod
    def attempt_login(cls,username, password):
        pass


    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        pass
        