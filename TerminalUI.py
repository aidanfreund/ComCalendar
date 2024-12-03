import threading
import re
import sys
from LoginMenu import LoginMenu
from InputController import InputController

class Terminal_UI():
    def run():
        while True:
            profile = Terminal_UI.login_statement()
            option_bool = True
            while option_bool:
                option_bool = Terminal_UI.select_option(profile)
                if option_bool is False:
                    break
                selection = input("Type quit or q to exit, type anything else to select another option again: ")
                selection.lower()
                if selection == "quit" or selection == "q":
                    sys.exit()

    def login():
        username = input("Enter username: ")
        while re.search("^[a-zA-Z1-9]*$",username) is None:
            username = input("Enter valid username: ")

        password = input("Enter password: ")
        while re.search("^[a-zA-Z1-9!]*$",password) is None:
            password = input("Enter valid password: ")

        login_menu = LoginMenu()
        login_bool = login_menu.login(username,password)
        if login_bool is not True:
            print("Failed to login")
            return False
        return True
        

    def create_account():
        username = input("Enter username: ")
        while re.search("^[a-zA-Z1-9]*$",username) is None:
            username = input("Enter valid username: ")

        password = input("Enter password: ")
        while re.search("^[a-zA-Z1-9]*$",password) is None:
            password = input("Enter valid password: ")

        login_menu = LoginMenu()
        profile = login_menu.create_profile(username,password)
        if profile is None:
            print("Failed to create profile")
            return None
        return profile

    def select_option(profile):
        input_selection = input("Enter Selection Number: "
                                +"\n1. Logout\n2. Upload Calendar to Profile"
                                +"\n3. Show Profile's Calendars\n4. Exit")
        match input_selection:
            case 1:
                return False
            case 2:
                Terminal_UI.upload_calendar(profile)
            case 3:
                Terminal_UI.show_calendar_list()
            case 4:
                sys.exit()
            case _:
                print("Invalid Selection")
            
    def login_statement():
        while True:
            input_selection = input("Login(L) or Create Account(CA) or Exit(E): ")
            input_selection = input_selection.lower()
            if input_selection == "l" or input_selection == "login":
                login_bool = Terminal_UI.login()
                while login_bool is not True:
                    profile = Terminal_UI.login()
                return profile
            elif input_selection == "ca" or input_selection == "create account":
                while profile is None:
                    profile = Terminal_UI.create_account()
                return profile
            elif input_selection == "e" or input_selection == "exit":
                sys.exit()
            else:
                print("Invalid Input")

    def upload_calendar(profile):
        calendar_string = input("Enter calendar file: ")
        calendar_name = input('Enter calendar name: ')
        InputController.upload_calendar(calendar_string,calendar_name)

    