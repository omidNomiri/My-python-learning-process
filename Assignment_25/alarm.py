from time import localtime ,sleep
from PySide6.QtCore import QThread, Signal
from alarm_database import Database

class Alarm_thread(QThread):
    alarm_signal = Signal()

    def __init__(self):
        super().__init__()
        self.data_base = Database()
        self.current_time = localtime()
        self.current_hour = self.current_time.tm_hour
        self.current_minute = self.current_time.tm_min

    def run(self):
        while True:
            sleep(1)
            on_alarm = []
            list_of_alarm = self.data_base.get_alarms()

            for alarm in list_of_alarm :
                if alarm[3] == 0 :
                    alarm_time = alarm[1].split (" : ")
                    on_alarm.append ({"id" : alarm[0] , "hour" : alarm_time[0] , "minute" : alarm_time[1] , "title" : alarm[2]})

                if alarm["hour"] == self.current_hour and \
                alarm["minute"] == self.current_minute:
                        print("ring")
                        text = f"{alarm['title']}\n{alarm['hour']} : {alarm['minute']}"
                        self.alarm_signal.emit(text)
