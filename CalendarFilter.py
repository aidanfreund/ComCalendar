from Calendar import Calendar
class CalendarFilter(Calendar):
    def FilterByDates(self, StartTime, EndTime):
        return any(StartTime <= event['date'] <= EndTime for event in self.Events)
    
    def FilterByTask(self, task):
        return any(event['task'] == task for event in self.Tasks)
    
    def FilterByEvent(self, event):
        return any(thing['event'] == event for thing in self.Events)
    
    