#Commit
# import LoginMenu
# import InputController
# import FactoryProducer
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



#move to other classes
# class Selection(Enum):
#     CREATE = 1
#     AGGREGTE = 2
#     CLONE = 3
#     DELETE = 4
#     COMPARE = 5
#     LOGOUT = 6
#     UPLOAD = 7
    # def Run():
    #     FactoryProducer.CreateFactory("MySQL")
    #     isLoggedIn = LoginMenu.Login("username", "password")
    #     if isLoggedIn:
    #         print("logged in")
    #     while(isLoggedIn):
    #         choice = input("Enter Your Choice:")
    #         InputController.selectOption(choice)
    #         if choice == "LOGOUT":
    #             isLoggedIn = False 
    # def DeleteProfile():
    #     pass



if __name__ == "__main__":
    main()