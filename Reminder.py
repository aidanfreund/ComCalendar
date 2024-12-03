#Reminder class for Calendar
#Contributers: Edwin Chavez


import datetime

class Reminder():

    #Constructor
    def __init__(self, reminder_id, date:datetime):
        self._reminder_id = reminder_id
        self._time = date.datetime
    
    #Returns the Unique ReminderID
    def get_id(self):
        return self._reminder_id
    
    #Returns the Date and Time of the Reminder
    def get_time(self):
        return self._time
    
    
    #Sets the Date and Time for the Reminder
    def set_time(self, date:datetime):
        self.date = date.datetime
        return True





    

