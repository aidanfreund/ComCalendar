#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime


class Task(Happening):
    def __init__(self, name, time, desc = ""):
        super().__init__(name, time, desc)
        self._completed = False

    def get_completed(self):
        return self._completed
    
    def flip_completed(self):
        self._completed = not(self._completed)
