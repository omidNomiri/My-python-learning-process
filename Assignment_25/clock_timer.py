from PySide6.QtCore import QThread, Signal

class Timer_thread(QThread):
    timer_finished_signal = Signal()

    def __init__(self):
        super().__init__()
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.end = False

    def run(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.end = False

        while True:
            if self.end:
                break

            self.sleep(1)
            self.second -= 1

            if self.second < 0:
                self.second += 60
                self.minute -= 1

            if self.minute < 0:
                self.minute += 60
                self.hour -= 1

            if self.hour == 0 and self.minute == 0 and self.second == 0:
                self.end = True
                self.timer_finished_signal.emit()
