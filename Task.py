#Aidan
#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime

class Task(Happening):
    def __init__(self, task_ID, name, time, desc = ""):
        super().__init__(task_ID, name, desc, time)
        self._completed = False

    def get_completed(self):
        return self._completed
    
    def set_completed(self,bool):
        self._completed = bool
    
    def set_first_time(self,time):
        self._first_time = time

    def set_description(self,description):
        self._description = description

    def set_name(self,name):
        self._name = name

    def get_id(self):
        return self._hap_id
    
    def get_first_time(self):
        return self._first_time
    
    def get_description(self):
        return self._description
    
    def get_name(self):
        return self._name
