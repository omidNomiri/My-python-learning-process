import time
from PySide6.QtCore import QThread, Signal


class world_clock_thread(QThread):
    world_clock_signal = Signal(int, int, int, str)

    def __init__(self):
        super().__init__()
        self._prev_time = None

    def run(self):
        while True:
            self.sleep(1)

            current_time = int(time.time())
            if current_time != self._prev_time:
                self._prev_time = current_time

                hours_iran = (current_time // 3600 + 3) % 24
                minutes_iran = (current_time // 60) % 60
                seconds_iran = current_time % 60

                hours_germany = (current_time // 3600 + 1) % 24
                minutes_germany = (current_time // 60) % 60
                seconds_germany = current_time % 60

                hours_usa = (current_time // 3600 - 8) % 24
                minutes_usa = (current_time // 60) % 60
                seconds_usa = current_time % 60

                self.world_clock_signal.emit(
                    hours_iran, minutes_iran, seconds_iran, "iran")
                self.world_clock_signal.emit(
                    hours_germany, minutes_germany, seconds_germany, "germany")
                self.world_clock_signal.emit(
                    hours_usa, minutes_usa, seconds_usa, "usa")
