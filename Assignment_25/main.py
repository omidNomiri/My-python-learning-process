from sys import argv
from functools import partial
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox
from ui_main_window import Ui_MainWindow
from world_clock import world_clock_thread
from clock_timer import Timer_thread

class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.msg_box = QMessageBox()
        self.ui.setupUi(self)
        self.ui.input_hour_text.setText("00")
        self.ui.input_minute_text.setText("00")
        self.ui.input_second_text.setText("00")

        self.world_clock = world_clock_thread()
        self.world_clock.start()
        self.world_clock.world_clock_signal.connect(self.show_world_clock)

        self.timer = Timer_thread()
        self.timer.timer_finished_signal.connect(self.timer_finished)

    def show_world_clock(self ,hour ,minute ,second ,country):
        if country == "iran":
            self.ui.iran_show_time_lb.setText(f"{hour}:{minute}:{second}")
        elif country == "germany":
            self.ui.germany_show_time_lb.setText(f"{hour}:{minute}:{second}")
        elif country == "usa":
            self.ui.usa_show_time_lb.setText(f"{hour}:{minute}:{second}")

    def start_timer(self):
        if self.ui.input_hour_text.text() == "":
            hour = 0
        else:
            hour = int(self.ui.input_hour_text.text())

        if self.ui.input_minute_text.text() == "":
            minute = 0
        else:
            minute = int(self.ui.input_minute_text.text())

        if self.ui.input_second_text.text() == "":
            second = 0
        else:
            second = int(self.ui.input_second_text.text())

        self.timer.run(hour, minute, second)
        self.timer.start()

    def timer_finished(self):
        self.msg_box.setText("time end")
        self.msg_box.exec()

    def reset_timer(self):
        self.ui.input_hour_text.setText("00")
        self.ui.input_minute_text.setText("00")
        self.ui.input_second_text.setText("00")

if __name__ == "__main__":
    app = QApplication(argv)
    window = Clock()

    window.ui.start_timer_button.clicked.connect(partial(window.start_timer))
    window.ui.reset_input_timer_button.clicked.connect(partial(window.reset_timer))

    window.show()
    app.exec()
