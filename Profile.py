class Profile():
    calendar_ID = 0

    def __init__(self, username:str, profile_ID: int, calendars:list):
        self.userName = username
        self.profile_ID = profile_ID
        self.calendars = calendars

    def get_calendars(self):
        print(self.calendars)
        print("getting calendar list")

    def get_profile_ID(self):
        return self.profile_ID
    
    def get_user_name(self):
        return self.userName
    
    def set_user_name(self,name_in):
        self._userName = name_in