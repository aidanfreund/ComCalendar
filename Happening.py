#Implementing the Happening Class
#Contributers: Edwin Chavez
import datetime


class Happening():

    #Experimental - Not really required as Python doesn't need to initialize null variables.
    """int(_hap_id)
    str(_name)
    Reminder(_reminder = [])
    str(_description)
    datetime(_first_time)"""

    #Constructor
    def __init__(self, hap_id, name, reminder, description, first_time):
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
    
    def set_name(self,name_in):
        self._name = name_in
    
    #Returns The Description
    def get_description(self):
        return self._description
    
    def set_description(self,description_in):
        self._description = description_in
    
    #Returns the First Time associated
    def get_first_time(self):
        return self._first_time
    
    #sets the first time associated
    def set_first_time(self, time:datetime):
        self._first_time = time

    #Edits The Specific Reminder Object
    def edit_reminder(self, reminder_id, date):
        self._reminder_id = reminder_id
        for id in self._reminder:
            if self._reminder_id == self._reminder[id]:
                self._reminder[id].date = date.date
                self._reminder[id].time = date.time
        return
    
    #Removes Reminder Object
    def remove_reminder(self, reminder_id):
        
        self._reminder_id = reminder_id

        count = 0 #Currently not useful, but will be in the Future

        for id in self._reminder:
            if self.reminder_id == self._reminder[id]:
                self._reminder.remove(id)
                count += 1 #Currently not useful but will be in the Future
        return 
    
    #Creates a new Reminder
    def create_reminder(self, reminder_id):
        self._reminder_id = reminder_id
        self._reminder.append(self._reminder_id)
        return