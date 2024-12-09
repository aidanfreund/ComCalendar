#Reminder class for Calendar
#Contributers: Edwin Chavez

import datetime

class Reminder():


    def __init__(self, reminder_id:int, notice_time:datetime):
        self._reminder_id = reminder_id
        self._time = notice_time
    
    def get_id(self):
        return self._reminder_id
    
    def get_time(self):
        return self._time
    
    def set_time(self, time:datetime):
        self.date = time
        return True
  
