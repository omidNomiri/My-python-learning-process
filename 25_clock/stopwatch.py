from PySide6.QtCore import QThread, Signal


class Stop_watch_thread(QThread):
    stop_watch_signal = Signal(int, int, int)

    def __init__(self):
        super().__init__()
        self.hour = 00
        self.minute = 00
        self.second = 00

    def run(self):
        while True:
            self.sleep(1)
            self.second += 1

            if self.second == 60:
                self.second = 0
                self.minute += 1

            if self.minute == 60:
                self.minute = 0
                self.hour += 1

            self.stop_watch_signal.emit(self.hour, self.minute, self.second)
