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

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()

     window.show()
     app.exec()
