from sys import argv
from functools import partial
from PySide6.QtWidgets import QMainWindow ,QApplication ,QMessageBox ,QLabel ,QPushButton ,QCheckBox
from PySide6.QtGui import QFontDatabase ,QFont
from ui_main_window import Ui_MainWindow
from world_clock import world_clock_thread
from clock_timer import Timer_thread
from stopwatch import Stop_watch_thread
from alarm import Alarm_thread
from alarm_database import Database

class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.msg_box = QMessageBox()
        self.ui.setupUi(self)
        self.ui.input_hour_text.setText("00")
        self.ui.input_minute_text.setText("00")
        self.ui.input_second_text.setText("00")
        self.seven_segment_font = "Assignment_25/src/DSEG7Modern-Regular.ttf"
        QFontDatabase.addApplicationFont("Assignment_25/src/DSEG7Modern-Regular.ttf")

        self.data_base = Database()
        self.list_of_alarm = []

        self.world_clock = world_clock_thread()
        self.world_clock.start()
        self.world_clock.world_clock_signal.connect(self.show_world_clock)

        self.timer = Timer_thread()
        self.timer.timer_finished_signal.connect(self.timer_finished)

        self.stop_watch = Stop_watch_thread()
        self.stop_watch.stop_watch_signal.connect(self.show_stop_watch)

        self.alarm = Alarm_thread()
        self.show_alarm()
        self.alarm.alarm_signal.connect(self.check_alarm)

    def show_world_clock(self, hour, minute, second, country):
        if country == "iran":
            self.ui.iran_show_time_lb.setText(f"{hour} : {minute} : {second}")
        elif country == "germany":
            self.ui.germany_show_time_lb.setText(f"{hour} : {minute} : {second}")
        elif country == "usa":
            self.ui.usa_show_time_lb.setText(f"{hour} : {minute} : {second}")

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
        self.ui.input_hour_text.setText(str(hour))
        self.ui.input_minute_text.setText(str(minute))
        self.ui.input_second_text.setText(str(second))

    def timer_finished(self):
        self.msg_box.setText("time end")
        self.msg_box.exec()

    def reset_timer(self):
        self.ui.input_hour_text.setText("00")
        self.ui.input_minute_text.setText("00")
        self.ui.input_second_text.setText("00")

    def start_stop_watch(self):
        self.stop_watch.start()
        self.stop_watch.run()

    def show_stop_watch(self, hour, minute, second):
        self.ui.show_stopwatch_label.setText(f"{hour} : {minute} : {second}")
        print(f"{hour}:{minute}:{second}")

    def stop_stop_watch(self):
        self.stop_watch.terminate()

    def set_alarm(self):
        new_title = self.ui.input_title_linetext.text()
        new_h = self.ui.input_hour_text_alarm.text()
        new_min = self.ui.input_minute_text_alarm.text()
        new_time = f"{new_h} : {new_min}"
        if self.data_base.add_alarm(new_time, new_title) == False:
            self.msg_box.setWindowTitle("❌Error!!❌")
            self.msg_box.exec()

        else:
            self.ui.input_hour_text_alarm.setText("0")
            self.ui.input_minute_text_alarm.setText("0")
            self.ui.input_title_linetext.setText("")
            self.show_alarm()

    def show_alarm(self):
        self.alarm_list = self.data_base.get_alarms()
        self.alarm_checkbox = []
        self.alarm_delete_button = []

        for row in range(len(self.alarm_list)):
            new_checkbox = QCheckBox()
            new_label_time = QLabel()
            new_label_title = QLabel()
            new_button = QPushButton()

            self.alarm_checkbox.append(
                {"checkbox": new_checkbox, "id": self.alarm_list[row][0], "mode": self.alarm_list[row][3]})
            self.alarm_delete_button.append(
                {"button": new_button, "id": self.alarm_list[row][0]})

            print(self.alarm_list[row][1], self.alarm_list[row][2])
            new_label_time.setText(self.alarm_list[row][1])
            new_label_time.setFont(QFont("Assignment_25/src/DSEG7Modern-Regular.ttf" ,18))
            new_label_title.setText(self.alarm_list[row][2])
            new_button.setText("X")
            new_button.setStyleSheet("background-color: rgb(255, 20, 0)")
            if self.alarm_list[row][3] == 0:
                new_checkbox.setChecked(True)

            new_button.clicked.connect(
                partial(self.delete_alarm, self.alarm_list[row][0]))

            self.ui.grid_layout_alarm.addWidget(new_checkbox, row, 0)
            self.ui.grid_layout_alarm.addWidget(new_label_time, row, 1)
            self.ui.grid_layout_alarm.addWidget(new_label_title, row, 2)
            self.ui.grid_layout_alarm.addWidget(new_button, row, 3)

    def check_alarm(self):
        self.msg_box.setWindowTitle("RING")
        self.msg_box.setText("ring")
        self.msg_box.exec()

    def delete_alarm(self, id):
        if self.data_base.delete_alarm(id) == False:
            self.msg_box.setWindowTitle("❌Error!!❌")
            self.msg_box.setText("Please try again later")
            self.msg_box.exec()


if __name__ == "__main__":
    app = QApplication(argv)
    window = Clock()

    window.ui.start_timer_button.clicked.connect(partial(window.start_timer))
    window.ui.reset_input_timer_button.clicked.connect(
        partial(window.reset_timer))
    window.ui.start_stopwatch_button.clicked.connect(
        partial(window.start_stop_watch))
    window.ui.stop_stopwatch_button.clicked.connect(
        partial(window.stop_stop_watch))
    window.ui.add_alarm_button.clicked.connect(partial(window.set_alarm))

    window.show()
    app.exec()
