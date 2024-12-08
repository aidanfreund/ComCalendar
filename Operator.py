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
from Happening import Happening

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
import os

class Operator:

    factory:DatabaseFactory = FactoryProducer("Profile").factory
    db_profile:DBProfile = factory.DB_profile


    #Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, calendar_obj:Calendar, description = ""):
        #add to db
        id = cls.db_profile.add_event(description, start_time, end_time, name, calendar_obj)
        #add to machine
        calendar_obj.add_event(id, name, start_time, end_time, description)
        return True

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
        cls.db_profile.delete_calendar(calendar_obj)
        #delete on machine
        profile_obj.delete_calendar(calendar_obj)
        pass

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
            #get cal obj
            cals = profile_obj.get_calendars()
            for cal in cals:
                if cal.get_calendar_id() == id:
                    calendar = cal
                    break
            #find current time, and convert to utc tme
            today = datetime.now()
            today = today.replace(tzinfo=timezone.utc)
            # Iterate through events in the .ics file and add them to the Calendar
            for ics_event in ics_calendar.events:
                desc = ics_event.name
                start = ics_event.begin
                end = ics_event.end

                #Create an object and add it to the Calendar
                #ics only has events, if start and end time are the same, interperate the event as a task
                
                if start != end:
                    id = cls.db_profile.add_event(desc, start, end, name, cls.db_profile.read_calendars())
                    calendar.add_event(id, name, start, end, desc)
                else:
                    task = Task(id, desc, start)
                    #assume tasks in past are completed
                    if start < today:
                        task.set_completed(False)
                    calendar.add_task(task)

            return True
        else:
            return False
    # downloads desired calendar to desired path
    # Returns .ics file string 
    @classmethod
    def download_calendar(cls, calendar:Calendar, file_path:str):
        """Simply takes a calendar and a file path  to write to, and writes the file in ics format
        if no path is provided it will save to the desktop with the calendar name"""
        
        #ensure the directory path exists
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        #set default path to user desktop
        if file_path == "":
            file_path = os.path.join(os.path.expanduser("~"), "Desktop") 
            file_path = os.path.join(file_path, calendar.get_calendar_name())    
        #force ics file type
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

        return f"{file_path}"
        

     # Copies a calendar and adds it to profile, returns true if successful

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
        return happ_obj.edit_reminder(id, time)

        

     # Filters calendar by events, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_events(cls, calendar_obj, start_date, end_date):

        pass


    # Filters calendar by tasks, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj, start_date, end_date):
        pass
    
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        pass

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, name:str, description:str, time:datetime, calendar_obj:Calendar):
        #add in db
        id = cls.db_profile.add_task(description,time,name, calendar_obj)
        #add in machine
        calendar_obj.add_task(id, time, name, description)
        
        return True

    # Removes/deletes an task from calendar, returns true if successful
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
        mach = happ_obj.remove_reminder(reminder_obj.get_id())

        return (db and mach)

    # Edits a reminder object, returns true if successful
    @classmethod
    def edit_reminder(cls, reminder_obj:Reminder, new_time:datetime):
        #update on machine
        reminder_obj.set_time(new_time)
        #attempt update in db
        return cls.db_profile.change_reminder(reminder_obj)

    # Deletes profile obj, returns true if successful
    @classmethod
    def delete_profile(cls, profile_obj):
        pass

   
    #Logs in to profile using username and password
    #Returns profile obj if a match exists
    @classmethod
    def login(cls,username, password):
        pass


    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        pass
        
"""from Profile import Profile
from DBProfile import DBProfile
from Calendar import Calendar
from DBFactory import DatabaseFactory, FactoryProducer
from DBConnection import DatabaseConnection
from datetime import timezone, datetime

from Profile import Profile
from Calendar import Calendar
from Event import Event
from Task import Task

from ics import Calendar as ICS_Calendar
from ics import Event as ICS_Event
import os

class Operator:

    factory:DatabaseFactory = FactoryProducer("Profile")
    db_profile:DBProfile = factory.DB_profile


    #Creates new event with attributes, returns true if successful
    @classmethod
    def add_event(cls, name, start_time, end_time, calendar_obj:Calendar, description = ""):
        #add to db
        id = cls.db_profile.add_event(description, start_time, end_time, name, calendar_obj)
        #add to machine
        calendar_obj.add_event(id, name, start_time, end_time, description)
        return True

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

    # Processes .ics file string and returns a boolean indicating its success
    @classmethod
    def upload_calendar(cls, name:str, file_path:str, profile_obj:Profile):
        reads an ICS file to create a calendar obj.  provided a file path to read from, 
        a name for the calendar, and the profile obj to be added to.
        will return calendar object. assumes user is in UTC time zone 
        (in order to reduce required downloads)
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
    def download_calendar(cls):
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
    def filter_calendar_by_events(cls, calendar_obj, start_date, end_date):
        pass


    # Filters calendar by tasks, returns a filtered calendar obj
    @classmethod
    def filter_calendar_by_tasks(cls, calendar_obj, start_date, end_date):
        pass
    
     # Filters calendar by dates, returning a new filtered calendar obj
    @classmethod
    def filter_calendar_by_dates(cls, calendar_obj, start_date, end_date):
        pass

    # Adds task to a calendar, returns true if successful
    @classmethod
    def add_task(cls, description, due_date, calendar_obj):
        pass

    # Removes an task from calendar, returns true if successful
    @classmethod
    def remove_task(cls, task_obj, calendar_obj):
        pass

    # Edits a task, returns true if successful
    @classmethod
    def edit_task(cls, description, due_date, task_obj):
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
    def login(cls,username, password):
        pass


    #Creates a profile obj and returns it 
    @classmethod
    def create_profile(cls, username, password):
        pass
        
"""