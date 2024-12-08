#Event.py
#Event class, type of Happening that inlcudes a second time
from Happening import Happening
import datetime

class Event(Happening):
    def __init__(self, task_ID:int, name:str, first_time:datetime, second_time:datetime, desc:str):
        super().__init__(task_ID, name, first_time, desc)
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
    def create_reminder(self, reminder_id):
        if reminder_id < 0:
            return False
        self._reminder_id = reminder_id
        self._reminder.append(self._reminder_id)
        return True
