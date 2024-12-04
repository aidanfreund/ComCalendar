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

    def retrieve_tasks(self):
        return self._tasks
    
    def retrieve_events(self):
        return self._events
    
    def add_task(self, hap_id, name, datetime):
        self._tasks.append(hap_id)
        return True
    
    def add_event(self, hap_id, name, start_time, end_time ):
        self._events.append(hap_id)
        return True        

    def delete_task(self, hap_id):
        try:
            for task in self._tasks:
                if task.get_id() == hap_id:
                    self._tasks.remove(hap_id)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False

    def delete_event(self, hap_id):
        try:
            for event in self._events:
                if event.get_id() == hap_id:
                    self._tasks.remove(hap_id)
            return True
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )
            return False
