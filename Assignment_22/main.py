import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.db = Database()
          self.tasks = self.db.get_task()

          for i in range(len(self.tasks)):
               new_task_box = QCheckBox()
               new_label = QLabel()
               new_label.setText(self.tasks[i][1])

               self.ui.form_Layout.addWidget(new_task_box)
               self.ui.form_Layout.addWidget(new_label)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()

     window.show()
     app.exec()
