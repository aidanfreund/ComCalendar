#Event.py
#Event class, type of Happening that inlcudes a second time
from Happening import Happening
import datetime
from Reminder import Reminder

def main():
    date_obj = datetime.datetime(2024, 2, 28, 17, 30, 0)
    date_obj2 = datetime.datetime(2024, 11, 27, 17, 30, 0)
    rem = Reminder(4, date_obj)
    test_event = Event(1, "no", rem, "desc...", date_obj, date_obj2)
    print(test_event.get_second_time())
    test_event.set_second_time(datetime.datetime.now())
    print(test_event.get_second_time())


class Event(Happening):
    def __init__(self, task_ID:int, name:str, reminder:Reminder, desc:str, first_time:datetime, second_time:datetime):
        super().__init__(task_ID, name, reminder, desc, first_time)
        self._second_time = second_time
        
    def get_second_time(self):
        return self._second_time
    
    def set_second_time(self, time:datetime):
        self._second_time = time 
    
    def set_name(self,name:str):
        self._name = name

if __name__ == "__main__":
    main()