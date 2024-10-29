class Calendar:
    def __init__(self, CalendarID, CalendarName, Events, Tasks):
        self._CalendarID = CalendarID
        self._CalendarName = CalendarName
        self._Events = Events if Events is not None else []
        self._Tasks = Tasks if Tasks is not None else []

    def GetCalendarID(self):
        return self._CalendarID
    
    def SetCalendar(self, CalendarID):
        self._CalendarId = CalendarID

    def GetCalendarName(self):
        return self._CalendarName

    def SetCalendarName(self, CalendarName):
        self._CalendarName = CalendarName

    def RetrieveTasks(self):
        return self._Tasks
    
    def RetrieveEvents(self):
        return self._Events
    
    def AddTask(self, Task):
        self._Tasks.append(Task)
    
    def AddEvent(self, Event):
        self._Events.append(Event)

    def DeleteTask(self, hapID):
        try:
            self._Tasks.remove(hapID)
        except ValueError:
            print(f"Task ID '{hapID}' not found." )

    def DeleteEvent(self, hapID):
        try:
            self._Tasks.remove(hapID)
        except ValueError:
            print(f"Event Id '{hapID}' not found.")

    