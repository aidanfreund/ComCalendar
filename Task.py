#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime
from Reminder import Reminder

class Task(Happening):
    def __init__(self, task_ID, name, time, desc):
        super().__init__(task_ID, name, desc, time)
        self._completed = False

    def get_completed(self):
        return self._completed
    

    def set_completed(self,bool):
        self._completed = bool
        return True
    
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
    
    def get_reminder(self):
        return self._reminder

    #Edits The Specific Reminder Object
    def edit_reminder(self, reminder_id:int, date:datetime):
        if reminder_id >-1:
            self._reminder_id = reminder_id
            for id in self._reminder:
                if self._reminder_id == self._reminder[id]:
                    self._reminder[id].date = date.date
                    self._reminder[id].time = date.time
            return True
        else:
            return False
    #Removes Reminder Object
    def remove_reminder(self, reminder_id):
        for id in self._reminder:
            if self.reminder_id == self._reminder[id]:
                self._reminder.remove(id)
                return True
        
        return False
    
    #Creates a new Reminder
    def create_reminder(self, reminder_id,time:datetime):
        if reminder_id <0:
            return False
        self._reminder = Reminder(reminder_id,time)
        return True
    
    def set_reminder(self,reminder:Reminder):
        self._reminder = reminder
