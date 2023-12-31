import string
import secrets
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow

class Generator(QMainWindow):
     def __init__(self):
          super().__init__()
          self.message_box = QMessageBox()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.alphabetic_chr = string.ascii_letters
          self.numerical_chr = string.digits
          self.special_chr = string.punctuation
          self.password = ""

     def get_length(self):
          self.length = int(self.ui.length_text.text())

     def select_mode(self, rdbtn_mode):
          self.mode = rdbtn_mode

     def generate(self):
          self.get_length()
          self.characters = ...

          if self.mode == "normal":
              self.characters = self.alphabetic_chr
          elif self.mode == "strong":
              self.characters = self.alphabetic_chr + self.numerical_chr
          elif self.mode == "very strong":
              self.characters = self.alphabetic_chr + self.numerical_chr + self.special_chr

          for _ in range(self.length):
               self.password += secrets.choice(self.characters)

          self.ui.password_output.setText(str(self.password))

          window.message_box.setWindowTitle("Completed")
          window.message_box.setText("five password generate for you.")
          window.message_box.exec()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Generator()

     window.ui.radio_normal.clicked.connect(partial(window.select_mode, "normal"))
     window.ui.radio_strong.clicked.connect(partial(window.select_mode, "strong"))
     window.ui.radio_very_strong.clicked.connect(partial(window.select_mode, "very strong"))

     window.ui.generate.clicked.connect(window.generate)

     window.show()
     app.exec()
