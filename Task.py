#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime

class Task(Happening):
    def __init__(self, task_ID, name, time, desc):
        super().__init__(task_ID, name, desc, time)
        self._completed = False

    def get_completed(self):
        return self._completed
    
    def flip_completed(self):
        self._completed = not(self._completed)
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

    #Edits The Specific Reminder Object
    def edit_reminder(self, reminder_id:int, date:datetime):
        self._reminder_id = reminder_id
        for id in self._reminder:
            if self._reminder_id == self._reminder[id]:
                self._reminder[id].date = date.date
                self._reminder[id].time = date.time
        return True
    
    #Removes Reminder Object
    def remove_reminder(self, reminder_id):
      
        self._reminder_id = reminder_id

        for id in self._reminder:
            if self.reminder_id == self._reminder[id]:
                self._reminder.remove(id)
                return True
                
        return False
    
    #Creates a new Reminder
    def create_reminder(self, reminder_id):
        self._reminder_id = reminder_id
        self._reminder.append(self._reminder_id)
        return True
