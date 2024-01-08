import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_main_window import Ui_MainWindow

class Game(QMainWindow):
     def __init__(self):
          super().__init__()
          self.message_box = QMessageBox()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.pc1_score = 0
          self.pc2_score = 0
          self.player_score = 0
          self.play_round = 0
          self.winner = None
          self.list_of_hand = ["✋", "🤚"]

     def play_player(self, hand_position):
          if self.play_round <= 5:
               if hand_position == "palm":
                    self.ui.btn_player.setText("✋")
               elif hand_position == "on_hand":
                    self.ui.btn_player.setText("🤚")
               self.play_computer(self.ui.btn_pc_1)
               self.play_computer(self.ui.btn_pc_2)
               self.check_winner()
               self.play_round += 1
          else:
               title = "Equal"
               if self.pc1_score < self.player_score and self.pc2_score < self.player_score:
                    self.winner = "Player"
               elif self.player_score < self.pc1_score and self.pc2_score < self.pc1_score:
                    self.winner = "Pc 1"
               elif self.pc1_score < self.pc2_score and self.player_score < self.pc2_score:
                    self.winner = "Pc 2"
               else:
                    title = "Equal"
                    self.winner = "No one"
               window.message_box.setWindowTitle(f"{title}")
               window.message_box.setText(f"{self.winner} Win")
               window.message_box.exec()

     def play_computer(self, button):
          number = random.randint(0, 1)
          hand = self.list_of_hand[number]
          button.setText(str(hand))

     def check_winner(self):
          if (self.ui.btn_pc_1.text() == self.ui.btn_pc_2.text()) != self.ui.btn_player.text():
               self.player_score += 1
               self.ui.text.setText(f"pc 1: {self.pc1_score}  pc 2: {self.pc2_score}  player: {self.player_score}")
          elif (self.ui.btn_pc_2.text() == self.ui.btn_player) != self.ui.btn_pc_1.text():
               self.pc1_score += 1
               self.ui.text.setText(f"pc 1: {self.pc1_score}  pc 2: {self.pc2_score}  player: {self.player_score}")
          elif (self.ui.btn_pc_1.text() == self.ui.btn_player) != self.ui.btn_pc_2.text():
               self.pc2_score += 1
               self.ui.text.setText(f"pc 1: {self.pc1_score}  pc 2: {self.pc2_score}  player: {self.player_score}")

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Game()

     window.ui.btn_palm.clicked.connect(partial(window.play_player, "palm"))
     window.ui.btn_on_hand.clicked.connect(partial(window.play_player, "on_hand"))

     window.show()
     app.exec()
