from Happening import Happening
from Task import Task
from Event import Event
from datetime import datetime

class Calendar:
    def __init__(self, calendar_id, calendar_name, events, tasks):
        self._calendar_id = calendar_id
        self._calendar_name = calendar_name
        self._events = events if events is not None else []
        self._tasks = tasks if tasks is not None else []


    def get_calendar_id(self):
        return self._calendar_id
    
    def set_calendar(self, calendar_id):
        self._calendar_id = calendar_id

    def get_calendar_name(self):
        return self._calendar_name

    def set_calendar_name(self, calendar_name):
        self._calendar_name = calendar_name

    def retrieve_tasks(self):
        return self._tasks
    
    def retrieve_events(self):
        return self._events
    
    def add_task(self, id:int, time:datetime, name:str, desc:str):
        task = Task(id, name, time, desc)
        self._tasks.append(task)
        return True
    
    def add_event(self, id:int, name:str, time1:datetime, time2:datetime, desc:str):
        event = Event(id, name, time1, time2, desc)
        self._events.append(event)
        return True
  
    #removes task from task array. using the id associated with task
    def delete_task(self, hap_id:int):
        try:
            for task in self._tasks:
                if task.get_id() == hap_id:
                    self._tasks.remove(task)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False
          
    #removes event from event array. using the id associated with event
    def delete_event(self, hap_id:int):
        try:
            for event in self._events:
                if event.get_id() == hap_id:
                    self._events.remove(event)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False


###Test
def compare_calendars(calendar1:Calendar, calendar2:Calendar):
    
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
    while i < len(free_slots1) and j < len(free_slots2) and slots < 6:
        start1, end1 = free_slots1[i]
        start2, end2 = free_slots2[j]
        # Find the overlapping time slot
        start_shared = max(start1, start2)
        end_shared = min(end1, end2)
        if start_shared < end_shared:
            shared_freetime + f"slot {slots}: {start_shared} -> {end_shared}\n"
        # Move to the next free slot
        if end1 < end2:
            i += 1
        else:
            j += 1

    return shared_freetime
