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
        print(f"adding task: {task.get_first_time()}")
        for i, etask in enumerate(self._tasks):
            print(f"Comparing {time} with {etask}")
            if time < etask:
                print(f"inserting at {i}")
                self._tasks.insert(i, task.get_first_time())
                return True
        print("appended to end")
        self._tasks.append(task.get_first_time())
        return True
    def add_event(self, id:int, name:str, time1:datetime, time2:datetime, desc:str):
        event = Event(id, name, time1, time2, desc)
        print(f"adding event: {event.get_second_time()}")
        for i, e_event in enumerate(self._events):
            print(f"Comparing {time1} with {e_event}")
            if time1 < e_event:
                self._events.insert(i, event.get_second_time())
                return True
        self._events.append(event.get_second_time())
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
        
    def __str__(self):
        task_string = [str(task) for task in self._tasks]
        event_string = [str(event) for event in self._events]
        return f"Claendar '{self._calendar_name}' :\nTasks:\n" + "\n".join(task_string)+"\nEvents:\n"+ "\n".join(event_string) 
        
