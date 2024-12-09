#Profile.py
#implementation of Profile class

#It is solely my fault (aidan) for this not being wrong in the Class Diagram
# missing delete_calendar(Calendar) and list parameters in create_new_calendar

from Calendar import Calendar

class Profile():
    def __init__(self, username:str, profile_id: str, calendars:list = []):
        self._username = username
        self._profile_id = profile_id
        self._calendars = calendars

    def get_calendars(self):
        return self._calendars
    
    def get_profile_id(self):
        return self._profile_id
    
    def get_username(self):
        return self._username
    
    #take a name and id to create a new calendar
    def create_new_calendar(self, id:int, name:str, events = [], tasks = []):
        #indicates error in database
        if id == -1:
            return False
        self._calendars.append(Calendar(id, name, events, tasks))
        return True
    
    #derefferences calendar from profile obj
    def delete_calendar(self, cal:Calendar):
        #simply dereference to delete
        self._calendars.remove(cal)
        return True
