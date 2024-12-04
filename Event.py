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
    
    def set_first_time(self, time):
        self._first_time = time

    def set_name(self,name):
        self._name = name

    def set_description(self,description):
        self._description = description

    def get_first_time(self):
        return self._first_time
    
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
    
    def get_id(self):
        return self._hap_id
