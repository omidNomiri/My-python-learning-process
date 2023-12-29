from numbers import Number
import sys
from functools import partial
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.unique_list = []
        self.buttons = [
            [self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
            [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
            [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
            [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]
        ]

        while len(self.unique_list) < 16:
            random_number = randint(1, 16)
            if random_number not in self.unique_list:
                self.unique_list.append(random_number)

        self.unique_list_2D = [self.unique_list[i:i+4] for i in range(0, len(self.unique_list), 4)]

        for i in range(4):
            for j in range(4):
                number = self.unique_list_2D[i][j]
                self.buttons[i][j].setText(str(number))
                self.buttons[i][j].clicked.connect(partial(self.play, i, j))
                if number == 16:
                    self.buttons[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j

    def play(self, i, j):
        if (i == self.empty_i and abs(j - self.empty_j) == 1 and j != self.empty_j) or \
            (j == self.empty_j and abs(i - self.empty_i) == 1 and i != self.empty_i):

            number = int(self.buttons[i][j].text())
            self.buttons[self.empty_i][self.empty_j].setText(str(number))
            self.buttons[i][j].setText("16")

            self.buttons[self.empty_i][self.empty_j].setVisible(True)
            self.buttons[i][j].setVisible(False)
            self.empty_i = i
            self.empty_j = j

if __name__ == "__main__":
    app = QApplication(sys.argv)

    game = Game()
    game.show()

    app.exec()
