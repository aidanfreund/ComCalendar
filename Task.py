#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime


class Task(Happening):
    def __init__(self, id:int, name:str, time:datetime, desc = ""):
        super().__init__(id, name, time, desc)
        self._completed = False

    def get_completed(self):
        return self._completed
    
    def set_completed(self, completion:bool):
        self._completed = completion
        return True
