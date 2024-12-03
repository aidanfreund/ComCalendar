
from Calendar import Calendar

class Profile():
    calendar_ID = 0

    def __init__(self, username:str, profile_ID: str, calendars:list):
        self.userName = username
        self.profile_ID = profile_ID
        self.calendars = calendars

    def getCalendars(self):
        print(self.calendars)
        print("getting calendar list")

    def getProfileID(self):
        return self.profile_ID
    
    def getUserName(self):
        return self.userName
    
    def createCalendar(self, ID:int, name:str):
        if len(self.calendars)>5:
            print("Profile has too many calendars, must have less than 6 in order to make a new calendar")
            return False
        self.calendars.append(Calendar.__init__(self, Profile.calendar_ID, name, [], []))
        Profile.calendar_ID += 1
        print("New Calendar Created")
        return True


