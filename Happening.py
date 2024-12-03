#Implementing the Happening Class
#Contributers: Edwin Chavez
import datetime

from abc import ABC, abstractmethod
from Reminder import Reminder

class Happening(ABC):
    
    #Abstract Class of Happening
        @abstractmethod
        def get_id(self):
            pass
        
        @abstractmethod
        def get_name(self):
            pass

        @abstractmethod
        def get_description(self):
            pass

        @abstractmethod
        def get_first_time(self):
            pass

        @abstractmethod
        def set_first_time(self, time:datetime):
            pass

        @abstractmethod
        def edit_reminder(self, reminder_id, date:datetime):
            pass
        
        @abstractmethod
        def remove_reminder(self, reminder_id):
            pass

        @abstractmethod
        def create_reminder(self, reminder_id):
            pass




'''
Not Sure if The bottom functions will just be implemented in the Task and Events Classes or If we will use
Inheritance and keep these here and use .super() in Task and Events Classes. So i have kept it here.

'''

class Its_Happening(Happening):
    #Constructor
    def __init__(self, hap_id:int, name:str, reminder, description:str, first_time:datetime):
        self._hap_id = hap_id
        self._name = name
        self._reminder = reminder
        self._description = description
        self._first_time = first_time

    #Returns the Happening Class ID
    def get_id(self):
        return self._hap_id
    
    #Returns the Name
    def get_name(self):
        return self._name
    
    #Returns The Description
    def get_description(self):
        return self._description
    
    #Returns the First Time Associated
    def get_first_time(self):
        return self._first_time
    #Sets the First Time Associated
    def set_first_time(self, time:datetime):
        self._first_time = time

    #Edits The Specific Reminder Object
    def edit_reminder(self, reminder_id:int, date:datetime):
        self._reminder_id = reminder_id
        self._reminder[reminder_id].set_time(date.datetime)
        return
    
    #Removes Reminder Object
    def remove_reminder(self, reminder_id):
        
        self._reminder_id = reminder_id
        if self._reminder_id in self._reminder:
            self._reminder.remove(self._reminder_id)
            return True
        else:
            return False
                
    
    #Creates a new Reminder
    def create_reminder(self, reminder_id):
        self._reminder_id = reminder_id
        self._reminder.append(self._reminder_id)
        return