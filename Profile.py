import LoginMenu
import InputController
import FactoryProducer
from Calendar import Calendar
from enum import Enum


def main(username, pswd):
    pass

class Selection(Enum):
    CREATE = 1
    AGGREGTE = 2
    CLONE = 3
    DELETE = 4
    COMPARE = 5
    LOGOUT = 6
    UPLOAD = 7

class Profile():
    userName = ""
    ProfileID = ""
    Calendars = Calendar[]


    def Run():
        FactoryProducer.CreateFactory("MySQL")

        isLoggedIn = LoginMenu.Login("username", "password")
        if isLoggedIn:
            print("logged in")

        while(isLoggedIn):
            choice = input("Enter Your Choice:")
            InputController.selectOption(choice)
            if choice == "LOGOUT":
                isLoggedIn = False 

    def DeleteProfile():

        pass



if __name__ == "__main()__":
    main()