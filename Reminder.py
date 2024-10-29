#Reminder class for Calendar
#Contributers: Edwin Chavez

import datetime

class Reminder:


    def __init__(self, reminder_id, time):
        self._reminder_id = reminder_id
        self._time = time
    
    #Returns the Unique ReminderID
    def get_reminder_id(self):
        return self._reminder_id
    
    #Returns the Date and Time of the Reminder
    def get_time(self):
        return self._time
    
    
    #Sets the Date and Time for the Reminder
    def set_time(self, date):
        self.date = date.date
        self.time = date.time


    

