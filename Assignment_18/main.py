from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial

class Game:
    def __init__(self):
        self.turn_player = 1
        self.message_box = None
        self.buttons = [[main_window.btn_number_1, main_window.btn_number_2, main_window.btn_number_3],
                        [main_window.btn_number_4, main_window.btn_number_5, main_window.btn_number_6],
                        [main_window.btn_number_7, main_window.btn_number_8, main_window.btn_number_9]]

    def show_message(self):
        self.message_box = QMessageBox()
        self.message_box.setWindowTitle("Congratulations")
        self.message_box.setText(f"Player {self.turn_player} wins")
        self.message_box.exec()

    def play(self, row, column):
        if self.turn_player == 1:
            self.buttons[row][column].setText("X")
            self.turn_player = 2
        elif self.turn_player == 2:
            self.buttons[row][column].setText("O")
            self.turn_player = 1
        self.check_winner()

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0].text() == self.buttons[row][1].text() == self.buttons[row][2].text() != "":
                if self.buttons[row][0].text() == "X":
                    self.show_message()
                else:
                    self.show_message()
            if self.buttons[0][row].text() == self.buttons[1][row].text() == self.buttons[2][row].text() != "":
                if self.buttons[0][row].text() == "X":
                    self.show_message()
                else:
                    self.show_message()
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == "X":
            self.show_message()
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == "X":
            self.show_message()
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() == "O":
            self.show_message()
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() == "O":  
            self.show_message()
        for row in range(3):
            for column in range(3):
                #if self.buttons[row][column].text() != "":
                    ...

loader = QUiLoader()
app = QApplication([])
main_window = loader.load("Assignment_18/main_window.ui")

game = Game()

for i in range(3):
    for j in range(3):
        game.buttons[i][j].clicked.connect(partial(game.play, i, j))

main_window.show()

app.exec()
