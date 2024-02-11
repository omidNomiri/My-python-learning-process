import time
from PySide6.QtCore import QThread ,Signal
from time_property import time_property

class world_clock_thread(QThread):
    world_clock_signal = Signal(time_property ,str)

    def run(self):
        while True:
            self.time = time.time()
            self.struct_time = time.gmtime(self.time)
            self.time_iran = time_property(self.struct_time.tm_hour ,self.struct_time.tm_min ,self.struct_time.tm_sec)
            self.time_iran.add(3 ,30 ,0)
            self.world_clock_signal.emit(self.time_iran ,"iran")

            self.time_germany = time_property(self.struct_time.tm_hour ,self.struct_time.tm_min ,self.struct_time.tm_sec)
            self.time_germany.add(5 ,0 ,0)
            self.world_clock_signal.emit(self.time_germany ,"germany")

            self.time_usa = time_property(self.struct_time.tm_hour ,self.struct_time.tm_min ,self.struct_time.tm_sec)
            self.time_usa.sub(1 ,0 ,0)
            self.world_clock_signal.emit(self.time_usa ,"usa")
