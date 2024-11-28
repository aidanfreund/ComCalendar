from Happening import Hapenning
class Calendar:
    def __init__(self, CalendarID, CalendarName, Events, Tasks):
        self._CalendarID = CalendarID
        self._CalendarName = CalendarName
        self._Events = Events if Events is not None else []
        self._Tasks = Tasks if Tasks is not None else []

    def get_calendarID(self):
        return self._CalendarID
    
    def set_calendar(self, CalendarID):
        self._CalendarId = CalendarID

    def get_calendarname(self):
        return self._CalendarName

    def set_calendarname(self, CalendarName):
        self._CalendarName = CalendarName

    def retrieve_tasks(self):
        return self._Tasks
    
    def retrieve_events(self):
        return self._Events
    
    def add_task(self, hap_id, name, Datetime):
        self._Tasks.append(hap_id)
    
    def add_event(self, hap_id, name, Starttime, EndTime ):
        self._Events.append(hap_id)
        

    def delete_task(self, hap_id):
        hap = Hapenning()
        hap_id = hap.get_id()
        try:
            self._Tasks.remove(hap_id)
        except ValueError:
            print(f"Task ID '{hap_id}' not found." )

    def delete_event(self, hap_id):
        hap = Hapenning()
        hap_id = hap.get_id()
        try:
            self._Tasks.remove(hap_id)
        except ValueError:
            print(f"Event Id '{hap_id}' not found.")

