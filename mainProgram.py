
from DBConnection import MySQLConnection
from DBProfile import MySQLProfile
from Profile import Profile
from Calendar import Calendar
import datetime
import time
from Task import Task
from Event import Event
from Reminder import Reminder

db_connection = MySQLConnection.get_db_connection()
if(db_connection != None):
    print("Working")


db_profile = MySQLProfile.get_db_profile()
result_profile_ID = db_profile.add_profile("abcd", "aaa")
if result_profile_ID > 0:
    print("Add profile Working")

test_profile = Profile("abcd",result_profile_ID,None)


result_calendar_ID = db_profile.add_calendar("Test1",test_profile)
if result_calendar_ID > 0:
    print("Add calendar working")

test_calendar = Calendar(result_calendar_ID,"Test1",None,None)


result_task_ID = db_profile.add_task("Test Description",datetime.datetime.now(),"Test Task",test_calendar)
if result_task_ID > 0:
    print("Add Task working")

result_event_ID = db_profile.add_event("Test Description", datetime.datetime.now(),datetime.datetime.now(),"Test Event",test_calendar)
if result_event_ID > 0:
    print("Add Event working")

test_event = Event(result_event_ID,"Test Event",datetime.datetime.now(),datetime.datetime.now(),"Test Description")
test_task = Task(result_task_ID,"Test Task",datetime.datetime.now(),"Test Description")

reminder_int = db_profile.add_reminder(datetime.datetime.now(),test_event)
if reminder_int > 0:
    print("Add reminder working")

test_reminder = Reminder(reminder_int,datetime.datetime.now())

reminder_bool = db_profile.change_reminder(test_reminder)
if reminder_bool:
    print("Change reminder working")

test_calendar.set_calendar_name("Test Change")

result_calendar_change = db_profile.change_calendar(test_calendar)
if result_calendar_change is True:
    print("Change Calendar Working")



test_task.set_completed(True)
test_task.set_first_time(datetime.datetime.now())
test_task.set_description("Test Description Change")
test_task.set_name("Test Name Change")
result_task_change = db_profile.change_task(test_task)
if result_task_change is True:
    print("Change Task working")

test_event.set_first_time(datetime.datetime.now())
test_event.set_name("Test Event Change")
test_event.set_description("Testing Event Description Change")
test_event.set_second_time(datetime.datetime.now())

result_event_change = db_profile.change_event(test_event)
if result_event_change is True:
    print("Change Event Working")

print("Read Profile: ")

print(db_profile.read_profile("abcd","aaa"))
print("Read Calendars: ")
print(db_profile.read_calendars(test_profile))
print("Read Events: ")
print( db_profile.read_events(test_calendar))
print("Read Tasks: ")
print(db_profile.read_tasks(test_calendar))
print("Read Reminder (Event): ")
print(db_profile.read_reminder(test_event))
test_reminder_two_id = db_profile.add_reminder(datetime.datetime.now(),test_task)
test_reminder_two = Reminder(test_reminder_two_id,datetime.datetime.now())
print("Read Reminder (Task): ")
print(db_profile.read_reminder(test_task))

result_reminder_bool = db_profile.delete_reminder(test_reminder)
if result_reminder_bool is True:
    print("Delete Reminder working")

result_event_bool = db_profile.delete_event(test_event)
if result_event_bool is True:
    print("Delete Event working")

result_task_bool = db_profile.delete_task(test_task)
if result_task_bool is True:
    print("Delete Task working")

result_calendar_bool = db_profile.delete_calendar(test_calendar)
if result_calendar_bool is True:
    print("Delete Calendar working")

result_profile_bool = db_profile.delete_profile(test_profile)
if result_profile_bool is True:
    print("Delete Profile working")