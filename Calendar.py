from Happening import Happening

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
        return True

    def get_calendar_name(self):

        return self._calendar_name

    def set_calendar_name(self, calendar_name):
        self._calendar_name = calendar_name
        return True

    def retrieve_tasks(self):
        return self._tasks
    
    def retrieve_events(self):
        return self._events
    
    def add_task(self, task):
        self._tasks.append(task)
        return True
    
    def add_event(self, event):
        self._events.append(event)
        return True
  
    #removes task from task array. using the id associated with task
    def delete_task(self, hap_id):
        try:
            for task in self._tasks:
                if task.get_id() == hap_id:
                    self._tasks.remove(task)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False
          
    #removes event from event array. using the id associated with event
    def delete_event(self, hap_id):
        try:
            for event in self._events:
                if event.get_id() == hap_id:
                    self._events.remove(event)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False
