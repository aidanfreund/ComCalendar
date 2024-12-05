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
        def edit_reminder(self, reminder_id, date):
            pass
        
        @abstractmethod
        def remove_reminder(self, reminder_id):
            pass

        @abstractmethod
        def create_reminder(self, reminder_id):
            pass

class Happening(Happening):
    #Constructor
    def __init__(self, hap_id, name, first_time, description = ""):
        self._hap_id = hap_id
        self._name = name
        self._description = description
        self._first_time = first_time

    #Returns the Happening Class ID
    def get_id(self):
        return self._hap_id
    
    #Returns the Name
    def get_name(self):
        return self._name
    
    def set_name(self,name_in):
        self._name = name_in
        return True
    
    #Returns The Description
    def get_description(self):
        return self._description
    
    def set_description(self, desc):
        self._description = desc
        return True

    #Returns the First Time Associated
    def get_first_time(self):
        return self._first_time
      
    #Sets the First Time Associated
    def set_first_time(self, time:datetime):
        self._first_time = time
        return True

    #Edits The Specific Reminder Object
    def edit_reminder(self, reminder_id, date):
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