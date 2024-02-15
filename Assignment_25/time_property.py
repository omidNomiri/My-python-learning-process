import time


class time_property():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def plus(self):
        self.second += 1

        if self.second == 60:
            self.second = 0
            self.minute += 1

        if self.minute == 60:
            self.minute = 0
            self.hour += 1

    def minus(self):
        if self.second > 0:
            self.second -= 1

        elif self.second == 0 and self.minute > 0:
            self.minute -= 1
            self.second = 59

        elif self.minute == 0 and self.hour > 0:
            self.hour -= 1
            self.minute = 59
            self.second = 59

    def add(self, hour, minute, second):
        self.hour += hour
        self.minute += minute
        self.second += second
        if self.second >= 60:
            self.second -= 60
            self.minute += 1

        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1

        if self.hour >= 24:
            self.hour -= 24

    def sub(self, hour, minute, second):
        self.hour -= hour
        self.minute -= minute
        self.second -= second
        if self.second < 0:
            self.second += 60
            self.minute -= 1

        if self.minute < 0:
            self.minute += 60
            self.hour -= 1

        if self.hour < 0:
            self.hour += 24
