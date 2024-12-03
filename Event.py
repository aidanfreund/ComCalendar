# Aidan
#Event.py
#Event class, type of Happening that inlcudes a second time
from Happening import Happening
import datetime
from Reminder import Reminder

class Event(Happening):
    def __init__(self, task_ID:int, name:str, reminder:Reminder, first_time:datetime, second_time:datetime, desc = ""):
        super().__init__(task_ID, name, reminder, first_time, desc)
        self._second_time = second_time
        
    def get_second_time(self):
        return self._second_time
    
    def set_second_time(self, time:datetime):
        self._second_time = time 
