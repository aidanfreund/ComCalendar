from Calendar import Calendar
import datetime

class CalendarFilter():
    def __init__(self, calendar:Calendar):
        self._calendar = calendar
        
    
    def filter_by_dates(self, start:datetime, end:datetime):
        """returns a calendar excluding events and tasks that start outside of the given time range """
        new_cal = Calendar(self._calendar.get_calendar_id(), self._calendar.get_calendar_name(), [], [])

        for event in self._calendar.RetrieveEvents():
            if (start <= event.get_first_time() <= end): # and second?
                new_cal.add_event(event)

        for task in self._calendar.RetrieveTasks():
            if start <= task.get_first_time() <= end:
                new_cal.add_task(task)

        return new_cal

    
    def filter_by_tasks(self, task):
        return self._calendar.retrieve_tasks()
    
    def filter_by_events(self, event):
        return self._calendar.retrieve_events()
    
    