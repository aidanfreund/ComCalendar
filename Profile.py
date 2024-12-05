from Calendar import Calendar

def main():
    test_profile = Profile("Aidan", 22, [2, 3, 4, 7, 6])

    cont = input("Create a calendar: ")
    while(cont == 'y'):
        name = input("Enter calendar name: ")
        test_profile.createCalendar(6, name)
        cont = input("Create another? ")
        
    pass


class Profile():
    calendar_ID = 0

    def __init__(self, username:str, profile_ID: str, calendars:list):
        self.userName = username
        self.profile_ID = profile_ID
        self.calendars = calendars

    def get_calendars(self):
        return self.calendars

    def get_profile_ID(self):
        return self.profile_ID
    
    def get_username(self):

        return self.userName
    
    def create_calendar(self, ID:int, name:str):
        if len(self.calendars)>5:
            print("Profile has too many calendars, must have less than 6 in order to make a new calendar")
            return False
        self.calendars.append(Calendar.__init__(self, Profile.calendar_ID, name, [], []))
        Profile.calendar_ID += 1
        print("New Calendar Created")
        return True

    def set_username(self,username):
        self.userName = username
