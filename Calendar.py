class Calendar:
    def __init__(self, _CalendarID, _CalendarName, _Events, _Tasks):
        self.CalendarID = _CalendarID
        self.CalendarName = _CalendarName
        self.Events = _Events if _Events is not None else []
        self.Tasks = _Tasks if _Tasks is not None else []

    def GetCalendarID(self):
        return self.CalendarID
    
    def SetCalendar(self, CalendarID):
        self.CalendarId = CalendarID

    def GetCalendarName(self):
        return self.CalendarName

    def SetCalendarName(self, CalendarName):
        self.CalendarName = CalendarName

    def RetrieveTasks(self):
        return self.Tasks
    
    def RetrieveEvents(self):
        return self.Events
    
    def AddTask(self, Task):
        self.Tasks.append(Task)
    
    def AddEvent(self, Event):
        self.Events.append(Event)

    def DeleteTask(self, hapID):
        try:
            self.Tasks.remove(hapID)
        except ValueError:
            print(f"Task ID '{hapID}' not found." )

    def DeleteEvent(self, hapID):
        try:
            self.Tasks.remove(hapID)
        except ValueError:
            print(f"Event Id '{hapID}' not found.")

    