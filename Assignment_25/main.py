from sys import argv
from functools import partial
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
from ui_main_window import Ui_MainWindow
from world_clock import world_clock_thread


class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.msg_box = QMessageBox()
        self.ui.setupUi(self)

        self.world_clock = world_clock_thread()
        self.world_clock.start()
        self.world_clock.world_clock_signal.connect(self.show_world_clock)

    def show_world_clock(self ,time ,country):
        if country == "iran":
            self.ui.iran_show_time_lb.setText(f"{time.hour}:{time.minute}:{time.second}")
        elif country == "germany":
            self.ui.germany_show_time_lb.setText(f"{time.hour}:{time.minute}:{time.second}")
        elif country == "usa":
            self.ui.usa_show_time_lb.setText(f"{time.hour}:{time.minute}:{time.second}")

if __name__ == "__main__":
    app = QApplication(argv)
    window = Clock()

    window.show()
    app.exec()
