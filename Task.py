#Task.py
#Task Class, a type of happening with completion status

from Happening import Happening
import datetime
from Reminder import Reminder

def main():
    date_obj = datetime.datetime.now()
    rem = Reminder(4, date_obj)
    test_task = Task(1, "no", rem, "desc...", date_obj)
    test_task.flip_completed()
    print(test_task.get_completed())
    test_task.flip_completed()
    print(test_task.get_completed())




class Task(Happening):
    def __init__(self, task_ID, name, reminder, desc, time):
        super().__init__(task_ID, name, reminder, desc, time)
        self._completed = False

    def get_completed(self):
        return self._completed
    
    def flip_completed(self):
        self._completed = not(self._completed)
    


if __name__ == "__main__":
    main()