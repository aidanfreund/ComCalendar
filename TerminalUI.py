import threading
import sys
import calendar
import datetime
from InputController import InputController

class TerminalUI():
    def run():
        while True:
            login_bool = TerminalUI.login_statement()
            while login_bool:
                login_bool = TerminalUI.select_option()
                if login_bool is False:
                    break
                selection = input("Type exit or e to exit, type anything else to select another option again: ")
                selection.lower()
                if selection == "exit" or selection == "e":
                    sys.exit()

    def login():
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_bool = InputController.login(username,password)
        if login_bool is not True:
            print("Failed to login")
            return False
        return True
        

    def create_account():
        username = input("Enter username or exit(e): ")
        if username == "exit" or username == "e":
            sys.exit()
        password = input("Enter password: ")
        profile_bool = InputController.create_profile(username,password)
        if profile_bool is False:
            print("Failed to create profile")
            return False
        return True

    def select_option():
        while True:
            input_selection = int(input("Enter Selection Number: "
                                    +"\n1. Logout\n2. Upload Calendar to Profile"
                                    +"\n3. Show Profile's Calendars\n4. Delete Profile"
                                    + "\n5. Exit"))
            match input_selection:
                case 1:
                    return False
                case 2:
                    TerminalUI.upload_calendar()
                case 3:
                    TerminalUI.show_calendar_list()
                case 4:
                    input_char = input("Are You sure?(y/n): ")
                    input_char.lower()
                    if input_char == "n":
                        print("Canceled Delete")
                    if input_char == "y":
                        bool_delete = InputController.delete_profile()
                        if bool_delete == "False":
                            print("Failed to delete")
                        else:
                            print("Delete successful")
                    
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
                login_bool = TerminalUI.login()
                while login_bool is not True:
                    profile_bool = TerminalUI.login()
                return profile_bool
            elif input_selection == "ca" or input_selection == "create account":
                while profile_bool is False:
                    profile_bool = TerminalUI.create_account()
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
        calendars = InputController.get_profile().get_calendars()
        while True:
            i = 0
            for element in calendars:
                print(f"{i+1}. Calendar: {element.get_calendar_name()}")
                i +=1
            while True:
                input_selection = input("Select Calendar to operate on, type add to add calendar, type aggregate to combine 2 calendars,"
                                        +"type compare to compare calendars, or type back to go back: ")
                if input_selection == "add":
                    TerminalUI.add_calendar()
                elif input_selection == "back":
                    return
                elif int(input_selection) > 0 and int(input_selection) < calendars.len():
                    TerminalUI.calendar_options(calendars[int(input_selection)])
                elif input_selection == "compare":
                    if calendars.len() < 2:
                        print("Not enough calendars to compare")
                    else:
                        TerminalUI.compare_calendars()
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
        calendar_one = int(input("Enter Number of first calendar: "))
        calendar_two = int(input("Enter Number of second calendar: "))
        calendar_compared = InputController.compare_calendars(InputController.get_calendar()[calendar_one],InputController.get_calendar()[calendar_two])
        print("Events: ")
        for event in calendar_compared.get_events():
            needwork
    
    def calendar_options():
        while True:
            calendar = InputController.get_calendar()
            print(calendar.get_calendar_name())
            TerminalUI.print_calendar()
            input_selection = int(input("Select Option Number:"
                                    + "\n1. Download Calendar \n2. View Events"
                                    + "\n3. View Tasks \n4. View All"
                                    + "\n5. Delete Calendar \n6. Create Copy of Calendar"
                                    + "\n7. Back"))
            match input_selection:
                case 1:
                    download_string = InputController.download_calendar()
                    print("File: ")
                    print(download_string)
                case 2: #view Events
                    TerminalUI.view_events()
                case 3: #view Tasks
                    TerminalUI.view_tasks()
                case 4: #veiw all
                    calendar = InputController.get_calendar()
                    i = 0
                    print("Events: ")
                    for event in calendar.get_events():
                        print(f"{i+1}. {event.get_name()} starts at {event.get_start_time()} and ends at {event.get_end_time()}")
                        i += 1
                    print("Tasks: ")
                    k = 0
                    for task in calendar.get_tasks():
                        print(f"{k+1}. {task.get_name()} starts at {task.get_start_time()} and Completion status: {task.get_completed()}")
                        k += 1    
                case 5:
                    check_input = input("Are you sure you want to delete the calendar?(y/n)")
                    check_input.lower()
                    if check_input == "y":
                        delete_bool = InputController.delete_calendar()
                        if delete_bool is True:
                            print("Deletion Successful")
                        else:
                            print("Deletion Failed")
                    else:
                        print("Deletion Stopped")
                case 6:
                    TerminalUI.copy_calendar()
                case 7:
                    return
                case _:
                    print("Invalid Input")

    def print_calendar():

        print(calendar.month_name[datetime.datetime.now().month], datetime.datetime.now().year)
        print("Mo\t  Tu \tWe\t  Th \tFr \t  Sa \tSu")

        month_days = calendar.monthcalendar(datetime.datetime.now().year, datetime.datetime.now().month)

        for week in month_days:
            for day in week:
                if day == 0:
                    print("    ", end="  ")
                else:
                    print(f"{day:2d}  ", end="  ")
            print()  

    def view_events():
        calendar = InputController.get_calendar()
        i = 0
        for event in calendar.get_events():
            print(f"{i+1}. {event.get_name()} starts at {event.get_start_time()} and ends at {event.get_end_time()}")
            i += 1
        while True:
            option_input = int(input("Select an Event number or 0 to go back"))
            if option_input > 0 and option_input < calendar.get_events().len():
                InputController.set_happening(calendar.get_events()[option_input])
                TerminalUI.event_options()
            elif option_input == 0:
                return
            else:
                print("Invalid Input")

    def view_tasks():
        calendar = InputController.get_calendar()
        i = 0
        for task in calendar.get_tasks():
            print(f"{i+1}. {task.get_name()} starts at {task.get_start_time()} and Completion status: {task.get_completed()}")
            i += 1
        while True:
            option_input = int(input("Select an Event number or 0 to go back"))
            if option_input > 0 and option_input < calendar.get_events().len():
                InputController.set_happening(calendar.get_tasks()[option_input])
                TerminalUI.task_options()
            elif option_input == 0:
                return
            else:
                print("Invalid Input")

    def event_options():
        pass
    def task_options():
        pass
    def reminder_options():
        pass
    def reminder_check():
        pass


    