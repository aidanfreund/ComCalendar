import threading
import sys
import calendar
import datetime
import time
from datetime import timedelta
from InputController import InputController
from Calendar import Calendar

thread_flag_lock = threading.Lock()
thread_flag = False


class TerminalUI():
    def run():
        while True:
            login_bool = TerminalUI.login_statement()
            while login_bool:
                login_bool = TerminalUI.select_option()
                if login_bool is False:
                    break
                selection = input("Type exit or e to exit, type anything else to select another option again: ")
                selection = selection.lower()
                if selection == "exit" or selection == "e":
                    sys.exit()

    def login():
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_bool = InputController.login(username,password)
        if login_bool is False:
            print("Failed to login")
            return False
        return True
        

    def create_account():
        username = input("Enter username or back: ")
        if username == "back":
            return
        password = input("Enter password: ")

        profile_bool = InputController.create_profile(username,password)
        if profile_bool is False:
            print("Failed to create profile")
            return False
        return True


    def select_option():
        while True:
            try:
                input_selection = int(input("Enter Selection Number: "
                                        +"\n1. Logout\n2. Upload Calendar to Profile"
                                        +"\n3. Show Profile's Calendars\n4. Delete Profile"
                                        + "\n5. Exit\n"))
                match input_selection:
                    case 1:
                        return False
                    case 2:

                        TerminalUI.upload_calendar()
                    case 3:
                        TerminalUI.show_calendar_list()
                    case 4:
                        input_char = input("Are You sure?(y/n): ")
                        input_char = input_char.lower()
                        if input_char == "n":
                            print("Canceled Delete")
                        elif input_char == "y":
                            bool_delete = InputController.delete_profile()
                            if bool_delete == False:
                                print("Failed to delete")
                            else:
                                print("Delete successful")
                        else:
                            print("Invalid Input")
                        
                    case 5:
                        sys.exit()
                    case _:
                        print("Invalid Selection")
            except ValueError:
                print("Invalid Input")
                continue
            
    def login_statement():
        login_bool = False
        while True:
            input_selection = input("Login(L) or Create Account(CA) or Exit(E): ")
            input_selection = input_selection.lower()
            if input_selection == "l" or input_selection == "login":

                login_bool = TerminalUI.login()
                while login_bool is not True:
                    login_bool = TerminalUI.login()
                return login_bool
            elif input_selection == "ca" or input_selection == "create account":
                while login_bool is False:
                    login_bool = TerminalUI.create_account()
                return login_bool
            elif input_selection == "e" or input_selection == "exit":
                sys.exit()
            else:
                print("Invalid Input")

    def upload_calendar():
        calendar_string = input("Enter calendar file: ")
        calendar_name = input('Enter calendar name: ')
        upload_calendar = InputController.upload_calendar(calendar_string,calendar_name)
        if upload_calendar is True:
            print("Upload successful")
        else:
            print("Failed to upload")

    def show_calendar_list():
        while True:
            calendars = InputController.get_profile().get_calendars()
            i = 0
            print()
            for element in calendars:
                print(f"{i+1}. Calendar: {element.get_calendar_name()}")
                i +=1
            print()
            try:
                input_selection = int(input("Select Option: \n1.Select Calendar to operate on \n2.Add Calendar"
                                        +"\n3.Combine 2 calendars \n4.Compare calendars"
                                        +"\n5. Back\n"))
                match input_selection:
                    case 1:
                        if len(calendars) < 1:
                            print("This profile has no calendars")
                            break
                        try:
                            calendar_number = int(input("Enter Calendar number: "))
                            if calendar_number < 1 or calendar_number > len(calendars):
                                print("Invalid Input")
                                break
                            else:
                                InputController.set_calendar(calendars[calendar_number - 1])
                                TerminalUI.calendar_options()
                        except ValueError:
                            print("Invalid Input")
                            continue
                    case 2:
                        TerminalUI.add_calendar()
                    case 3:
                        if len(calendars) < 2:
                            print("There are not 2 calendars to combine")
                        else:
                            try:
                                calendar_one = int(input("Enter first calendar number: "))
                                calendar_two = int(input("Enter second calendar number: "))

                                if calendar_one > len(calendars) or calendar_one < 1 or calendar_two > len(calendars) or calendar_two < 1:
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
                            except ValueError:
                                print("Invalid Input")
                    case 4:
                        if len(calendars) < 2:
                            print("Not enough calendars to compare")
                        else:
                            TerminalUI.compare_calendars()
                    case 5:
                        return
                    case _:
                        print("Invalid Input")
            except ValueError:
                print("Invalid Input")
                continue

    def add_calendar():
        calendar_name = input("Enter new Calendar's name: ")

        add_calendar_bool = InputController.create_calendar(calendar_name)
        if add_calendar_bool is True:
            print("Added Calendar Successfully")
        else:
            print("Failed to add Calendar")

    def compare_calendars():
        calendars = InputController.get_profile().get_calendars()
        calendar_one = int(input("Enter Number of first calendar: "))
        calendar_two = int(input("Enter Number of second calendar: "))

        if calendar_one > len(calendars) or calendar_one < 1 or calendar_two > len(calendars) or calendar_two < 1:
            print("Incorrect number selection of calendar")
        else:
            calendar_compared_string = InputController.compare_calendars(calendar_one - 1,calendar_two - 1)
            print(calendar_compared_string)
    
    def calendar_options():
        while True:
            calendar = InputController.get_calendar()
            print("Calendar Name: " + calendar.get_calendar_name())
            TerminalUI.print_calendar()

            try:
                input_selection = int(input("Select Option Number:"
                                        + "\n1. Download Calendar \n2. View Events"
                                        + "\n3. View Tasks \n4. View All Tasks and Events"
                                        + "\n5. View Tasks and Events Between specific dates"
                                        + "\n6. Add Event \n7. Add Task"
                                        + "\n8. Delete Calendar \n9. Create Copy of Calendar"
                                        + "\n10. Back\n"))
                with thread_flag_lock:
                    global thread_flag
                    thread_flag = True
                TerminalUI.reminder_check()
                match input_selection:
                    case 1:
                        download_string = InputController.download_calendar()
                        print("File: ")
                        print(download_string)
                    case 2: #view Events
                        if len(calendar.retrieve_events()) < 1:
                            print("No Events to show")
                        else:
                            TerminalUI.view_events()
                    case 3: #view Tasks
                        if len(calendar.retrieve_tasks()) < 1:
                            print("No Tasks to Show")
                        else:
                            TerminalUI.view_tasks()
                    case 4: #view all
                        if len(calendar.retrieve_events()) > 0:        
                            print(InputController.filter_calendar_by_events())
                        if len(calendar.retrieve_tasks()) > 0:
                            print(InputController.filter_calendar_by_tasks())
                        if len(calendar.retrieve_events()) == 0 and len(calendar.retrieve_tasks()) == 0:
                            print("No events or tasks to show")
                    case 5:#filter by dates
                        while True:
                            first_time_input = input("Enter start date in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                first_time = datetime.datetime.strptime(first_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                                continue
                        while True:
                            second_time_input = input("Enter end date in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                second_time = datetime.datetime.strptime(second_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                                continue
                        filter_date_string = InputController.filter_calendar_by_dates(first_time,second_time)
                        print(filter_date_string)
                    case 6:#add event
                        event_name = input("Enter name for Event: ")
                        event_description = input("Enter description of Event: ")
                        while True:
                            event_first_time_input = input("Enter start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_first_time = datetime.datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                                continue
                        while True:
                            event_second_time_input = input("Enter end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                            try:
                                event_second_time = datetime.datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                                continue
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
                                task_time = datetime.datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                                break
                            except ValueError:
                                print("Invalid Format")
                                continue 
                        create_task_bool = InputController.add_task(task_name,task_description,task_time) 
                        if create_task_bool is True:
                            print("Task added Successfully")
                        else:
                            print("Failed to add Task") 

                    case 8: #delete calendar
                        check_input = input("Are you sure you want to delete the calendar?(y/n): ")
                        check_input = check_input.lower()
                        if check_input == "y":
                            delete_bool = InputController.delete_calendar()
                            if delete_bool is True:
                                print("Deletion Successful")
                                with thread_flag_lock:
                                    thread_flag = False
                                InputController.set_calendar(None)
                                return
                            else:
                                print("Deletion Failed")
                        elif check_input == "n":
                            print("Deletion Stopped")
                        else:
                            print("Invalid Input")
                    case 9: #copy calendar
                        copy_bool = InputController.copy_calendar()
                        if copy_bool is True:
                            print("Copy successful")
                        else:
                            print("Failed to copy calendar")
                    case 10: #back
                        with thread_flag_lock:
                            thread_flag = False
                        return
                    case _:
                        print("Invalid Input")
            except ValueError:
                print("Invalid Input")
                continue

    def print_calendar():

        print(calendar.month_name[datetime.datetime.now().month], datetime.datetime.now().year)
        print("Mo    Tu    We    Th    Fr    Sa    Su")

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
        print(InputController.filter_calendar_by_events())
        while True:
            try:
                option_input = int(input("Select an Event number or 0 to go back: "))
                if option_input > 0 and option_input <= len(calendar.retrieve_events()):
                    InputController.set_happening(calendar.retrieve_events()[option_input - 1])
                    TerminalUI.event_options()
                    return
                elif option_input == 0:
                    return
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
                continue

    def view_tasks():
        calendar = InputController.get_calendar()
        print(InputController.filter_calendar_by_tasks())
        while True:
            try:
                option_input = int(input("Select an Task number or 0 to go back: "))
                if option_input > 0 and option_input <= len(calendar.retrieve_events()):
                    InputController.set_happening(calendar.retrieve_tasks()[option_input - 1])
                    TerminalUI.task_options()
                    return
                elif option_input == 0:
                    return
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
                continue

    def event_options():
        while True:
            if InputController.get_happening().get_reminder() is None:
                try:
                    input_option = int(input("Select operation for Event: "
                                    +"\n1. Edit Event \n2. Delete Event"
                                    +"\n3. Add Reminder \n4. Back\n"))
                    match input_option:
                        case 1:
                            name_input = input("Enter new Event name: ")
                            description_input = input("Enter new Description: ")
                            while True:
                                event_first_time_input = input("Enter new start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    event_first_time = datetime.datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
                            while True:
                                event_second_time_input = input("Enter new end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    event_second_time = datetime.datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
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
                                    reminder_time = datetime.datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
                            add_reminder_bool = InputController.create_reminder(reminder_time)
                            if add_reminder_bool is True:
                                print("Added Reminder successfully")
                            else:
                                print("Failed to add Reminder")
                        case 4:
                            return
                        case _:
                            print("Invalid Input")
                except ValueError:
                    print("Invalid Input")
                    continue

            else:
                try:
                    input_option = int(input("Select operation for Event: "
                                        +"\n1. Change Event \n2. Delete Event"
                                        +"\n3. View Reminder \n4. Back\n"))
                    match input_option:
                        case 1:
                            name_input = input("Enter new Event name: ")
                            description_input = input("Enter new Description: ")
                            while True:
                                event_first_time_input = input("Enter new start time of Event in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    event_first_time = datetime.datetime.strptime(event_first_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
                            while True:
                                event_second_time_input = input("Enter new end time of Event in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    event_second_time = datetime.datetime.strptime(event_second_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
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
                except ValueError:
                    print("Invalid Input")
                    continue    

    def task_options():
        task = InputController.get_happening()
        while True:
            if task.get_reminder() is None:
                try:
                    input_option = int(input("Select operation for Task: "
                                    +"\n1. Edit Task \n2. Delete Task"
                                    +"\n3. Add Reminder \n4.Complete Task"
                                    + "\n5. Back\n"))
                    match input_option:
                        case 1:
                            task_name = input("Enter new name for Task: ")
                            task_description = input("Enter new description of Task: ")
                            task_complete_input = input("Enter Completion Status(t/f): ")
                            task_complete_input = task_complete_input.lower()
                            if task_complete_input =="t":
                                task_completed = True
                            elif task_complete_input == "f":
                                task_completed = False
                            else:
                                print("Invalid Input, Defaulting to False")
                                task_completed = False     
                            while True:
                                task_time_input = input("Enter new time of Task in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    task_time = datetime.datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue 
                            create_task_bool = InputController.edit_task(task_name,task_description,task_time,task_completed) 
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
                                    reminder_time = datetime.datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
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
                except ValueError:
                    print("Invalid Input")
                    continue
                
            else:
                try:
                    input_option = int(input("Select operation for Task: "
                                        +"\n1. Edit Task \n2. Delete Task"
                                        +"\n3. View Reminder \n4. Complete Task"
                                        + "\n5. Back\n"))
                    match input_option:
                        case 1:
                            task_name = input("Enter new name for Task: ")
                            task_description = input("Enter new description of Task: ")
                            while True:
                                task_time_input = input("Enter new time of Task in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    task_time = datetime.datetime.strptime(task_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format") 
                                    continue
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
                except ValueError:
                    print("Invalid Input")
                    continue

    def reminder_options():
        print(f"Current Reminder Time: {InputController.get_reminder().get_time()}")
        while True:
            try:
                input_option = int(input("Select Option Number:"
                                + "\n1. Delete Reminder \n2. Edit Reminder"
                                + "\n3. Back\n"))
                match input_option:
                    case 1:
                        delete_reminder_bool = InputController.remove_reminder()
                        if delete_reminder_bool is True:
                            print("Reminder Deleted Successfully")
                            return
                        else:
                            print("Failed to delete Reminder")
                    case 2:
                        while True:
                                reminder_time_input = input("Enter new time of Reminder in the format (YYYY-MM-DD HH:MM) : ")
                                try:
                                    reminder_time = datetime.datetime.strptime(reminder_time_input,"%Y-%m-%d %H:%M")
                                    break
                                except ValueError:
                                    print("Invalid Format")
                                    continue
                        change_reminder_bool = InputController.create_reminder(reminder_time)
                        if change_reminder_bool is True:
                            print("Edited Reminder successfully")
                        else:
                            print("Failed to edit Reminder")
                    case 3:
                        return
                    case _:
                        print("Invalid Input")
            except ValueError:
                print("Invalid Input")
                continue

    def reminder_check():
        def check_reminders_in_calendar(calendar):
            global thread_flag
            while True:
                with thread_flag_lock:
                    if thread_flag is True:
                        for event in calendar.retrieve_events():
                            if event.get_reminder() == None:
                                break
                            if event.get_reminder().get_time() - timedelta(seconds = 60) <= datetime.datetime.now() <= event.get_reminder().get_time() + timedelta(seconds=60):
                                print(f"Event {event.get_name()} starts at: {event.get_first_time()}")
                        for task in calendar.retrieve_events():
                            if task.get_reminder() == None:
                                break
                            if task.get_reminder().get_time() - timedelta(seconds = 60) <= datetime.datetime.now() <= task.get_reminder().get_time() + timedelta(seconds=60):
                                print(f"Task {task.get_name()} time is: {task.get_first_time()}")
                    else:
                        break
                time.sleep(60)
        
        thread = threading.Thread(target=check_reminders_in_calendar, args=(InputController.get_calendar(),))
        thread.daemon = True
        thread.start()
    