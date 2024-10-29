#Implementing the Happening Class
#Contributers: Edwin Chavez

from Reminder import Reminder

class Hapenning(Reminder):

    #Experimental - Not really required as Python doesn't need to initilize null variables
    int(_hap_iD)
    str(_name)
    Reminder(_reminder = [])
    str(_description)

    #Constructor
    def __init__(self, hap_id, name, reminder, description):
        self._hap_id = hap_id
        self._name = name
        self._reminder = reminder
        self._description = description
    #Returns the Happening Class ID
    def get_id(self):
        return self._hap_id
    #Returns the Name
    def get_name(self):
        return self._name
    #Returns The Description
    def get_description(self):
        return self._description
    
    #Edits The Specific Reminder Object
    def edit_reminder():
        return
    #Removes Reminder Object
    def remove_reminder():
        return
    #Creates a new Reminder
    def create_reminder():
        return