import sys
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow

class Game(QMainWindow):
     def __init__(self):
          super().__init__()
          self.message_box = QMessageBox()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.movement_of_pc = ["🎱", "📄", "✂"]

     def pc_move(self):
          pc_movement = choice(self.movement_of_pc)
          self.ui.btn_pc.setText(str(pc_movement))

     def player_move(self, movement):
          if movement == "stone":
               self.ui.btn_pc.setText("🎱")
          elif movement == "paper":
               self.ui.btn_pc.setText("📄")
          elif movement == "scissors":
               self.ui.btn_pc.setText("✂")

     def check_winner(self):
          ...

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Game()

     window.ui.btn_stone.clicked.connect(window.player_move("stone"))
     window.ui.btn_paper.clicked.connect(window.player_move("paper"))
     window.ui.btn_scissors.clicked.connect(window.player_move("scissors"))

     window.show()
     app.exec()
