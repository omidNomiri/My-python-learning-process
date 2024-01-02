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
          self.list_of_pc_movement = ["🎱", "📄", "✂"]
          self.pc_movement = None

     def pc_move(self):
          self.pc_movement = choice(self.list_of_pc_movement)
          self.ui.btn_pc.setText(str(self.pc_movement))

     def player_move(self, player_movement):
          if player_movement == "stone":
               self.ui.btn_pc.setText("🎱")
          elif player_movement == "paper":
               self.ui.btn_pc.setText("📄")
          elif player_movement == "scissors":
               self.ui.btn_pc.setText("✂")
          self.pc_move()
          self.check_winner()

     def check_winner(self):
          if self.ui.btn_player.text() == self.ui.btn_pc.text():
               window.ui.result_text.setText("Game result: Equal")

          elif (self.ui.btn_player.text() == "🎱" and self.ui.btn_pc.text() == "✂") or \
               (self.ui.btn_player.text() == "📄" and self.ui.btn_pc.text() == "🎱") or \
               (self.ui.btn_player.text() == "✂" and self.ui.btn_pc.text() == "📄"):
               window.ui.result_text.setText("Game result: Player Win!")

          else:
               window.ui.result_text.setText("Game result: PC Win!")

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Game()

     window.ui.btn_stone.clicked.connect(window.player_move("stone"))
     window.ui.btn_paper.clicked.connect(window.player_move("paper"))
     window.ui.btn_scissors.clicked.connect(window.player_move("scissors"))

     window.show()
     app.exec()
