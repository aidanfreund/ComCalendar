#Implementing the Happening Class
#Contributers: Edwin Chavez
import datetime


from abc import ABC, abstractmethod
from Reminder import Reminder

class Happening(ABC):
    
    def __init__(self, hap_id, name, description, first_time, reminder=None):
        self._hap_id = hap_id
        self._name = name
        self._reminder = reminder
        self._description = description
        self._first_time = first_time
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
        def create_reminder(self, reminder_id,time):
            pass
