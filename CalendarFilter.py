from Calendar import Calendar
class CalendarFilter(Calendar):
    def FilterByDates(self, start_time, end_time):
        return any(start_time <= event['date'] <= end_time for event in self.events)
    
    def FilterByTask(self, task):
        return any(event['task'] == task for event in self.tasks)
    
    def FilterByEvent(self, event):
        return any(thing['event'] == event for thing in self.events)
