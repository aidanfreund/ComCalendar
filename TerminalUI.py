import threading
import sys
import calendar
import datetime
from InputController import InputController
from Calendar import Calendar

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
                    InputController.set_calendar(calendars[input_selection])
                    TerminalUI.calendar_options()
                elif input_selection == "compare":
                    if calendars.len() < 2:
                        print("Not enough calendars to compare")
                    else:
                        TerminalUI.compare_calendars()
                elif input_selection == "aggregate":
                    if calendars.len() < 2:
                        print("There are not 2 calendars to combine")
                    else:
                        calendar_one = int(input("Enter first calendar number: "))
                        calendar_two = int(input("Enter second calendar number: "))
                        if calendar_one > calendars.len() or calendar_one < 1 or calendar_two > calendars.len() or calendar_two < 1:
                            print("Incorrect number selection of calendar")
                        else:
                            new_calendar_name = input("Enter name for new Calendar: ")
                            calendar_output = InputController.aggregate_calendar((calendar_one - 1),(calendar_two - 1), new_calendar_name)
                            if type(calendar_output) is Calendar:
                                print("New Calendar Events: ")
                                for event in calendar_output.retrieve_events():
                                    print(f"Event name: {event.get_name()}, Description: {event.get_description()}")
                                    print(f"start time: {event.get_first_time()} , end time: {event.get_second_time()}")
                                    print()
                                print("New calendar Tasks: ")
                                for task in calendar_output.retrieve_tasks():
                                    print(f"Task name: {event.get_name()}, Description: {task.get_description()}")
                                    print(f"Time: {task.get_first_time()} , Completion status: {task.get_completed}")
                                    print()
                            else:
                                print("Failed to aggregate calendars")
                else:
                    print("Invalid Input")


    def add_calendar():
        calendar_name = input("Enter new Calendar's name: ")
        InputController.create_calendar(calendar_name)

    def compare_calendars():
        calendars = InputController.get_profile().get_calendars()
        calendar_one = int(input("Enter Number of first calendar: "))
        calendar_two = int(input("Enter Number of second calendar: "))
        if calendar_one > calendars.len() or calendar_one < 1 or calendar_two > calendars.len() or calendar_two < 1:
            print("Incorrect number selection of calendar")
        else:
            calendar_compared_string = InputController.compare_calendars((calendar_one - 1),(calendar_two - 1))
            print(calendar_compared_string)
    
    def calendar_options():
        while True:
            calendar = InputController.get_calendar()
            print(calendar.get_calendar_name())
            TerminalUI.print_calendar()
            input_selection = int(input("Select Option Number:"
                                    + "\n1. Download Calendar \n2. View Events"
                                    + "\n3. View Tasks \n4. View All Tasks and Events"
                                    + "\n5. View Tasks and Events Between specific dates"
                                    + "\n6.Add Event \n7. Add Task"
                                    + "\n8.Delete Calendar \n9. Create Copy of Calendar"
                                    + "\n10. Back"))
            match input_selection:
                case 1:
                    download_string = InputController.download_calendar()
                    print("File: ")
                    print(download_string)
                case 2: #view Events
                    TerminalUI.view_events()
                case 3: #view Tasks
                    TerminalUI.view_tasks()
                case 4: #view all
                    print(InputController.filter_calendar_by_events())
                    print(InputController.filter_calendar_by_tasks())
                case 5:#filter by dates
                    while True:
                        first_time_input = input("Enter start date in the format (YYYY-MM-DD HH:MM) : ")
                        try:
                            first_time = datetime.strptime(first_time_input,"%Y-%m-%d %H:%M")
                            break
                        except ValueError:
                            print("Invalid Format")
                    while True:
                        second_time_input = input("Enter start date in the format (YYYY-MM-DD HH:MM) : ")
                        try:
                            second_time = datetime.strptime(second_time_input,"%Y-%m-%d %H:%M")
                            break
                        except ValueError:
                            print("Invalid Format")
                    filter_date_string = InputController.filter_calendar_by_dates(first_time,second_time)
                    print(filter_date_string)
                case 6:#add event
                    event_name = input("Enter name for Event: ")
                    event_description = input("Enter description of Event: ")
                    while True:
                        event_first_time_input = input("Enter start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                        try:
                            event_first_time = datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                            break
                        except ValueError:
                            print("Invalid Format")
                    while True:
                        event_second_time_input = input("Enter end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                        try:
                            event_second_time = datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                            break
                        except ValueError:
                            print("Invalid Format")
                    create_event_bool = InputController.add_event(event_name,event_first_time,event_second_time,event_description)
                    if create_event_bool is True:
                        print("Event added Successfully")
                    else:
                        print("Failed to add Event")

                case 7: #add task
                    task_name = input("Enter name for Task: ")
                    task_description = input("Enter description of Task: ")
                    while True:
                        task_time_input = input("Enter time of Task in the format (YYYY-MM-DD HH:MM) : ")
                        try:
                            task_time = datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                            break
                        except ValueError:
                            print("Invalid Format") 
                    create_task_bool = InputController.add_task(task_name,task_description,task_time) 
                    if create_task_bool is True:
                        print("Task added Successfully")
                    else:
                        print("Failed to add Task") 

                case 8: #delete calendar
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
                case 9: #copy calendar
                    copy_bool = InputController.copy_calendar(calendar.get_calendar_id())
                    if copy_bool is True:
                        print("Copy successful")
                    else:
                        print("Failed to copy calendar")
                case 10: #back
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
        print(InputController.filter_calendar_by_events())
        while True:
            option_input = int(input("Select an Event number or 0 to go back"))
            if option_input > 0 and option_input < calendar.get_events().len():
                InputController.set_happening(calendar.get_events()[option_input])
                TerminalUI.event_options()
                return
            elif option_input == 0:
                return
            else:
                print("Invalid Input")

    def view_tasks():
        print(InputController.filter_calendar_by_tasks())
        while True:
            option_input = int(input("Select an Event number or 0 to go back"))
            if option_input > 0 and option_input < calendar.get_events().len():
                InputController.set_happening(calendar.get_tasks()[option_input])
                TerminalUI.task_options()
                return
            elif option_input == 0:
                return
            else:
                print("Invalid Input")

    def event_options():
        while True:
            if InputController.get_happening().get_reminder() is None:
                input_option = int(input("Select operation for Event: "
                                +"\n1. Edit Event \n2. Delete Event"
                                +"\n3. Add Reminder \n4. Back"))
                match input_option:
                    case 1:
                        name_input = input("Enter new Event name: ")
                        description_input = input("Enter new Description: ")
                        while True:
                            event_first_time_input = input("Enter new start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_first_time = datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        while True:
                            event_second_time_input = input("Enter new end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_second_time = datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        edit_event_bool = InputController.edit_event(name_input,event_first_time,event_second_time,description_input)
                        if edit_event_bool is True:
                            print("Event edited successfully")
                        else:
                            print("Failed to edit Event")
                    case 2:
                        delete_bool = InputController.delete_event()
                        if delete_bool is True:
                            print("Event Deleted Successfully")
                            InputController.set_happening(None)
                            return
                        else:
                            print("Failed to Delete Event")
                    case 3:
                        while True:
                            reminder_time_input = input("Enter time of Reminder in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                reminder_time = datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        add_reminder_bool = InputController.create_reminder(reminder_time)
                        if add_reminder_bool is True:
                            print("Added Reminder successfully")
                        else:
                            print("Failed to add Reminder")
                    case 4:
                        return
                    case _:
                        print("Invalid Input")

            else:
                input_option = int(input("Select operation for Event: "
                                    +"\n1. Change Event \n2. Delete Event"
                                    +"\n3. View Reminder \n4. Back"))
                match input_option:
                    case 1:
                        name_input = input("Enter new Event name: ")
                        description_input = input("Enter new Description: ")
                        while True:
                            event_first_time_input = input("Enter new start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_first_time = datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        while True:
                            event_second_time_input = input("Enter new end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_second_time = datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        edit_event_bool = InputController.edit_event(name_input,event_first_time,event_second_time,description_input)
                        if edit_event_bool is True:
                            print("Event edited successfully")
                        else:
                            print("Failed to edit Event")
                    case 2:
                        delete_bool = InputController.delete_event()
                        if delete_bool is True:
                            print("Event Deleted Successfully")
                            InputController.set_happening(None)
                            return
                        else:
                            print("Failed to Delete Event")
                    case 3:
                        InputController.set_reminder(InputController.get_happening().get_reminder())
                        TerminalUI.reminder_options()
                    case 4:
                        return
                    case _:
                        print("Invalid Input")
        

    def task_options():
        task = InputController.get_happening()
        while True:
            if task.get_reminder() is None:
                input_option = int(input("Select operation for Task: "
                                +"\n1. Edit Task \n2. Delete Task"
                                +"\n3. Add Reminder \n4.Complete Task"
                                + "\n5. Back"))
                match input_option:
                    case 1:
                        task_name = input("Enter new name for Task: ")
                        task_description = input("Enter new description of Task: ")
                        while True:
                            task_time_input = input("Enter new time of Task in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                task_time = datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format") 
                        create_task_bool = InputController.edit_task(task_name,task_description,task_time,task.get_completed()) 
                        if create_task_bool is True:
                            print("Task edited Successfully")
                        else:
                            print("Failed to edit Task")
                    case 2:
                        delete_task_bool = InputController.delete_task()
                        if delete_task_bool is True:
                            print("Task Successfully deleted")
                            InputController.set_happening(None)
                            return
                        else:
                            print("Failed to delete task")
                    case 3:
                        while True:
                            reminder_time_input = input("Enter time of Reminder in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                reminder_time = datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                        add_reminder_bool = InputController.create_reminder(reminder_time)
                        if add_reminder_bool is True:
                            print("Added Reminder successfully")
                        else:
                            print("Failed to add Reminder")
                    case 4:
                        if task.get_completed() is True:
                            print("Task already completed")
                            break
                        complete_task_bool = InputController.edit_task(task.get_name(),task.get_description(),task.get_first_time(),True)
                        if complete_task_bool is True:
                            print("Completed Task")
                        else:
                            print("Failed to complete Task")
                    case 5:#back
                        return
                    case _:
                        print("Invalid Input")
                
            else:
                input_option = int(input("Select operation for Event: "
                                    +"\n1. Edit Task \n2. Delete Task"
                                    +"\n3. View Reminder \n4. Complete Task"
                                    + "\n5. Back"))
                match input_option:
                    case 1:
                        task_name = input("Enter new name for Task: ")
                        task_description = input("Enter new description of Task: ")
                        while True:
                            task_time_input = input("Enter new time of Task in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                task_time = datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format") 
                        create_task_bool = InputController.edit_task(task_name,task_description,task_time,task.get_completed()) 
                        if create_task_bool is True:
                            print("Task edited Successfully")
                        else:
                            print("Failed to edit Task")
                    case 2:
                        delete_task_bool = InputController.delete_task()
                        if delete_task_bool is True:
                            print("Task Successfully deleted")
                            InputController.set_happening(None)
                            return
                        else:
                            print("Failed to delete task")
                    case 3:
                        InputController.set_reminder(task.get_reminder())
                        TerminalUI.reminder_options()
                    case 4:
                        if task.get_completed() is True:
                            print("Task already completed")
                            break
                        complete_task_bool = InputController.edit_task(task.get_name(),task.get_description(),task.get_first_time(),True)
                        if complete_task_bool is True:
                            print("Completed Task")
                        else:
                            print("Failed to complete Task")
                    case 5:#back
                        return
                    case _:
                        print("Invalid Input")

    def reminder_options():
        print(f"Current Reminder Time: {InputController.get_reminder().get_time()}")
        while True:
            input_option = int(input("Select Option Number:"
                            + "\n1. Delete Reminder \n2. Edit Reminder"
                            + "\n3. Back"))
            match input_option:
                case 1:
                    delete_reminder_bool = InputController.delete_reminder()
                    if delete_reminder_bool is True:
                        print("Reminder Deleted Successfully")
                        return
                    else:
                        print("Failed to delete Reminder")
                case 2:
                    while True:
                            reminder_time_input = input("Enter new time of Reminder in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                reminder_time = datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                    change_reminder_bool = InputController.create_reminder(reminder_time)
                    if change_reminder_bool is True:
                        print("Edited Reminder successfully")
                    else:
                        print("Failed to edit Reminder")
                case 3:
                    return
                case _:
                    print("Invalid Input")

    def reminder_check():
        


    