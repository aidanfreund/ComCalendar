import Profile
from enum import Enum

class InputController:
    # Options to be defined
    class Selection(Enum):
        OPTION1 = 1
        OPTION2 = 2
        OPTION3 = 3
    def create_calendar(self,calName):
        pass
    # Create new calendars from two calendars
    def aggregate_calendars(self, firstCalName, secondCalName):
        pass
    # Needs to return calendar object
    def clone_calendar(self,calName):
        pass
    # Deletes calendar
    def delete_calendar(self, calName):
        pass
    # Needs to return calendar object
    def compare_calendars(self, firstCalName, secondCalName):
        pass
    # Logout method to be discussed
    def logout(self):
        pass
    # Returns bool if successful
    def upload_calendar(self):
        pass
    # Does action based on option
    def select_option(self,OPTION):
        pass
