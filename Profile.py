from Calendar import Calendar

class Profile():

    def __init__(self, username:str, profile_id: str, calendars:list):
        self._username = username
        self._profile_id = profile_id
        self._calendars = calendars

    def get_calendars(self):
        return self._calendars
    
    def get_profile_id(self):
        return self._profile_id
    
    def get_username(self):
        return self._username
    
    def create_new_calendar(self, id:int, name:str):
        if len(self._calendars)>5:
            print("Profile has too many calendars, must have less than 6 in order to make a new calendar")
            return False
        self.calendars.append(Calendar.__init__(self, id, name, [], []))
        print("New Calendar Created")
        return True


