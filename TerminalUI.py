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
                selection = input("Type exit or e to exit, type anything else to select another option again: ")
                selection.lower()
                if selection == "exit" or selection == "e":
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
        username = input("Enter username or exit(e): ")
        if username == "exit" or username == "e":
            sys.exit()
        password = input("Enter password: ")

        login_menu = LoginMenu()
        profile_bool = login_menu.create_profile(username,password)
        if profile_bool is False:
            print("Failed to create profile")
            return False
        return True

    def select_option(profile):
        while True:
            input_selection = input("Enter Selection Number: "
                                    +"\n1. Logout\n2. Upload Calendar to Profile"
                                    +"\n3. Show Profile's Calendars\n4. Delete Profile"
                                    + "\n5. Exit")
            match input_selection:
                case 1:
                    return False
                case 2:
                    Terminal_UI.upload_calendar(profile)
                case 3:
                    Terminal_UI.show_calendar_list(profile)
                case 4:
                    input_char = input("Are You sure?(y/n): ")
                    input_char.lower()
                    if input_char == "n":
                        print("Canceled Delete")
                    if input_char == "y":
                        InputController.delete_profile()
                    
                case 5:
                    sys.exit()
                case _:
                    print("Invalid Selection")
            
    def login_statement():
        profile_bool = False
        while True:
            input_selection = input("Login(L) or Create Account(CA) or Exit(E): ")
            input_selection = input_selection.lower()
            if input_selection == "l" or input_selection == "login":
                login_bool = Terminal_UI.login()
                while login_bool is not True:
                    profile_bool =Terminal_UI.login()
                return profile_bool
            elif input_selection == "ca" or input_selection == "create account":
                while profile_bool is False:
                    profile_bool = Terminal_UI.create_account()
                return profile_bool
            elif input_selection == "e" or input_selection == "exit":
                sys.exit()
            else:
                print("Invalid Input")

    def upload_calendar():
        calendar_string = input("Enter calendar file: ")
        calendar_name = input('Enter calendar name: ')
        InputController.upload_calendar(calendar_string,calendar_name)

    def show_calendar_list():
        calendars = InputController.get_calendars()
        while True:
            i = 0
            for element in calendars:
                print(f"{i+1}. Calendar: {element.get_calendar_name()}")
                i +=1
            while True:
                input_selection = input("Select Calendar to operate on, type add to add calendar, type aggregate to combine 2 calendars,"
                                        +"type compare to compare calendars, or type back to go back: ")
                if input_selection == "add":
                    Terminal_UI.add_calendar()
                elif input_selection == "back":
                    return
                elif int(input_selection) > 0 and int(input_selection) < calendars.len():
                    Terminal_UI.calendar_options(calendars[int(input_selection)])
                elif input_selection == "compare":
                    if calendars.len() < 2:
                        print("Not enough calendars to compare")
                    else:
                        Terminal_UI.compare_calendars()
                elif input_selection == "aggregate":
                    if calendars.len() < 2:
                        print("There are not 2 calendars to combine")
                    else:
                        calendar_one = input("Enter first calendar number: ")
                        calendar_two = input("Enter second calendar number: ")
                        if int(calendar_one) > calendars.len() or int(calendar_one) < 1 or int(calendar_two) > calendars.len() or int(calendar_two) < 1:
                            print("Incorrect number selection of calendar")
                        else:
                            InputController.aggregate_calendar(calendars[int(calendar_one)],calendars[int(calendar_two)])
                else:
                    print("Invalid Input")


    def add_calendar():
        calendar_name = input("Enter new Calendar's name: ")
        InputController.create_calendar(calendar_name)

    def compare_calendars():
        calendar_one = input("Enter Number of first calendar: ")
        calendar_two = input("Enter Number of second calendar: ")
        calendar_compared = InputController.compare_calendars(InputController.get_calendar()[calendar_one],InputController.get_calendar()[calendar_two])
        print("Events: ")
        for event in calendar_compared.get_events():
            print("hello")

    def calendar_options():
        print("hello")
        # while True:
        #     input_selection = input("Select Option Number:"
        #                             + "\n1. Download Calendar \n2. ")
        

def main():
    Terminal_UI.run()

main()

    