import pytest
from Calendar import Calendar

class TestCalendar:
    def test_object_of_calendar(self):
        c = Calendar(1, "Calendar 1", [], [])
        print(c)