from random import randint
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial

class Game:
    def __init__(self):
        self.mode = None
        self.turn_player = "X"
        self.move = 1
        self.playerO_score = 0
        self.playerX_score = 0
        self.equal_score = 0
        self.main_window = loader.load("Assignment_18/main_window.ui")
        self.message_box = QMessageBox()
        self.buttons = [[self.main_window.btn_number_1, self.main_window.btn_number_2, self.main_window.btn_number_3],
                        [self.main_window.btn_number_4, self.main_window.btn_number_5, self.main_window.btn_number_6],
                        [self.main_window.btn_number_7, self.main_window.btn_number_8, self.main_window.btn_number_9]]

    def show_message(self):
        self.message_box.setWindowTitle("Congratulations")
        self.message_box.setText(f"Player {self.turn_player} wins")
        self.message_box.exec()

    def reload_game(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].setText("")
                self.buttons[row][column].setStyleSheet("background-color: rgb(232, 232, 232);")
        self.playerO_score = 0
        self.playerX_score = 0
        self.equal_score = 0
    
    def refresh_game(self):
        self.main_window.btn_player1_score.setText(f"player X score: {self.playerX_score}")
        self.main_window.btn_player2_score.setText(f"player O score: {self.playerO_score}")
        self.main_window.btn_equal.setText(f"equal: {self.equal_score} time")
        self.move = 0
        for row in range(3):
            for column in range(3):
                self.buttons[row][column].setText("")
                self.buttons[row][column].setStyleSheet("background-color: rgb(232, 232, 232);")

    def select_mode(self, change_mode):
        self.mode = change_mode

    def play(self, row, column):
        if self.mode == "PvP":
            if self.turn_player == "X":
                self.buttons[row][column].setText("X")
                self.buttons[row][column].setStyleSheet("color:Blue")
                self.main_window.btn_turn_O.setStyleSheet("color:Red")
                self.main_window.btn_turn_X.setStyleSheet("color:White")
                self.check_winner()
                self.turn_player = "O"
            elif self.turn_player == "O":
                self.buttons[row][column].setText("O")
                self.buttons[row][column].setStyleSheet("color:Red")
                self.main_window.btn_turn_O.setStyleSheet("color:White")
                self.main_window.btn_turn_X.setStyleSheet("color:Blue")
                self.check_winner()
                self.turn_player = "X"

        elif self.mode == "PvC":
            if self.turn_player == "X":
                self.buttons[row][column].setText("X")
                self.buttons[row][column].setStyleSheet("color:Blue")
                self.main_window.btn_turn_O.setStyleSheet("color:Red")
                self.main_window.btn_turn_X.setStyleSheet("color:White")
                self.check_winner()
                self.turn_player = "O"
            elif self.turn_player == "O":
                while True:
                    row = randint(0, 2)
                    column = randint(0, 2)
                    if self.buttons[row][column].text() == "":
                        self.buttons[row][column].setText("O")
                        self.buttons[row][column].setStyleSheet("color:Red")
                        self.main_window.btn_turn_O.setStyleSheet("color:White")
                        self.main_window.btn_turn_X.setStyleSheet("color:Blue")
                        break
                self.check_winner()
                self.turn_player = "X"

        else:
            self.message_box.setWindowTitle("Error Game mode")
            self.message_box.setText("Please select Game mode!")
            self.message_box.exec()

        self.move += 1

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0].text() == self.buttons[row][1].text() == self.buttons[row][2].text() != "":
                if self.buttons[row][0].text() == "X":
                    self.show_message()
                    self.playerX_score += 1
                    self.refresh_game()
                    return
                else:
                    self.show_message()
                    self.playerO_score += 1
                    self.refresh_game
                    return
            if self.buttons[0][row].text() == self.buttons[1][row].text() == self.buttons[2][row].text() != "":
                if self.buttons[0][row].text() == "X":
                    self.show_message()
                    self.playerX_score += 1
                    self.refresh_game()
                    return
                else:
                    self.show_message()
                    self.playerO_score += 1
                    self.refresh_game()
                    return
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == "X":
            self.show_message()
            self.playerX_score += 1
            self.refresh_game()
            return
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == "X":
            self.show_message()
            self.playerX_score += 1
            self.refresh_game()
            return
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == "O":
            self.show_message()
            self.playerO_score += 1
            self.refresh_game()
            return
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == "O":  
            self.show_message()
            self.playerO_score += 1
            self.refresh_game()
            return
        elif self.move == 9:
            self.equal_score += 1
            self.message_box.setWindowTitle("Congratulations")
            self.message_box.setText("All of Player win!")
            self.message_box.exec()
            self.refresh_game()
            return
        
    def about(self):
        self.message_box.setWindowTitle("About")
        self.message_box.setText("The Tic-Tac-Toe game you've implemented is a two-player game with two modes: Player vs. Player (PvP) and Player vs. Computer (PvC). The players take turns marking 'X' or 'O' on a 3x3 grid. The goal is to achieve a row, column, or diagonal of three of their marks before the opponent.")
        self.message_box.exec()

loader = QUiLoader()
app = QApplication([])

game = Game()

game.main_window.btn_turn_O.setStyleSheet("color:White")
game.main_window.btn_player1_score.setText(f"player X score: {game.playerX_score}")
game.main_window.btn_player2_score.setText(f"player O score: {game.playerO_score}")
game.main_window.btn_equal.setText(f"equal: {game.equal_score} time")

game.main_window.player_vs_player.clicked.connect(partial(game.select_mode, "PvP"))
game.main_window.player_vs_cpu.clicked.connect(partial(game.select_mode, "PvC"))
for i in range(3):
    for j in range(3):
        game.buttons[i][j].clicked.connect(partial(game.play, i, j))

game.main_window.btn_reload.clicked.connect(game.reload_game)
game.main_window.btn_about.clicked.connect(game.about)

game.main_window.show()

app.exec()
