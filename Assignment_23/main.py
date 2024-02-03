import sys
from random import randint
from sudoku import Sudoku
from functools import partial
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow, QApplication, QLineEdit, QFileDialog, QMessageBox, QSizePolicy
from ui_main_window import Ui_MainWindow

class SudokuGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.msg_box = QMessageBox()
        self.ui.setupUi(self)
        self.mode = 0
        self.win = True
        self.puzzle = Sudoku(3, seed=randint(0, 1000)).difficulty(0.5)

        self.ui.new_game_menu.triggered.connect(self.new_game)
        self.ui.open_file_menu.triggered.connect(self.open_file)
        self.ui.solve_menu.triggered.connect(self.solve)
        self.ui.about_menu.triggered.connect(self.about)
        self.ui.help_menu.triggered.connect(self.help)

        self.ui.dark_mode_toggle_btn.clicked.connect(partial(self.theme_toggle))
        self.ui.exit_btn.clicked.connect(partial(self.Exit))

        self.ui.dark_mode_toggle_btn.setText("🌑")
        self.line_text = [[None for row in range(9)] for column in range(9)]

        self.new_game()

    def new_game(self):
        self.puzzle = Sudoku(3, seed=randint(0, 1000)).difficulty(0.5)
        for row in range(9):
            for column in range(9):
                new_line_edit = QLineEdit()
                self.ui.grid_layout.addWidget(new_line_edit, row, column)
                new_line_edit.setAlignment((PySide6.QtCore.Qt.AlignCenter))
                new_line_edit.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                new_line_edit.textChanged.connect(partial(self.validation, row, column))
                self.line_text[row][column] = new_line_edit

                if self.puzzle.board[row][column] is not None:
                    new_line_edit.setText(str(self.puzzle.board[row][column]))
                    new_line_edit.setReadOnly(True)
                else:
                    new_line_edit.setText("")

    def solve(self):
        solved_puzzle = Sudoku.solve(self.puzzle)
        self.msg_box.setWindowTitle("Solve Sudoku")
        self.msg_box.setText(str(solved_puzzle))
        self.msg_box.exec()

    def about(self):
        self.msg_box.setWindowTitle("About")
        self.msg_box.setText("Sudoku is a logic-based combinatorial number-placement puzzle. In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid (also called boxes, blocks, or regions) contains all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.")
        self.msg_box.exec()

    def help(self):
        self.msg_box.setWindowTitle("Help")
        self.msg_box.setText("Sudoku grid consists of 9x9 spaces.\n You can use only numbers from 1 to 9.\n Each 3×3 block can only contain numbers from 1 to 9.\n Each vertical column can only contain numbers from 1 to 9.\n Each horizontal row can only contain numbers from 1 to 9.\n Each number in the 3×3 block, vertical column or horizontal row can be used only once.\n The game is over when the whole Sudoku grid is correctly filled with numbers.")
        self.msg_box.exec()

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open text file...')[0]

        with open(file_path, "r") as text_file:
            text = text_file.read()
            rows = text.split("\n")
            text_file_board = [[None for row in range(9)] for column in range(9)]
            for row in range(len(rows)):
                cells = rows[row].split(' ')
                for column in range(len(cells)):
                    text_file_board[row][column] = int(cells[column])

            for row in range(9):
                for column in range(9):
                    if text_file_board[row][column] != 0:
                        self.line_text[row][column].setText(str(text_file_board[row][column]))
                        self.line_text[row][column].setReadOnly(True)
                    else:
                        self.line_text[row][column].setText("")
                        self.line_text[row][column].setReadOnly(False)

    def theme_toggle(self):
        if self.mode == 0:
            self.ui.dark_mode_toggle_btn.setText("🌕")
            self.setStyleSheet("background-color: #404040; color: white;")
            self.mode = 1
        elif self.mode == 1:
            self.ui.dark_mode_toggle_btn.setText("🌑")
            self.setStyleSheet("")
            self.mode = 0

    def validation(self, row, column, text):
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_text[row][column].setText("")

        self.check(self.line_text)
        self.check_winner()

    def check(self, board):
        for row in range(9):
            for i in range(9):
                for j in range(9):
                    if self.line_text[row][i].text() == self.line_text[row][j].text() and i != j and self.line_text[row][i].text() != '':
                        self.line_text[row][i].setStyleSheet("color: red;")

        for col in range(9):
            for i in range(9):
                for j in range(9):
                    if self.line_text[i][col].text() == self.line_text[j][col].text() and i != j and self.line_text[i][col].text() != '':
                        self.line_text[i][col].setStyleSheet("color: red;")

        for row_start in range(0, 9, 3):
            for column_start in range(0, 9, 3):
                number_in_box = set()
                for row in range(row_start, row_start+3):
                    for col in range(column_start, column_start+3):
                        number = board[row][col]
                        if number in number_in_box:
                            self.line_text[row][col].setStyleSheet("color:red;")
                            return False
                        number_in_box.add(number)
        return True

    def check_winner(self):
        solved_puzzle = Sudoku.solve(self.puzzle)
        for i in range(len(self.line_text)):
            for j in range(len(self.line_text)):
                if solved_puzzle[i][j] != self.puzzle[i][j]:
                    self.win = False
        if self.win == True:
            self.msg_box.setWindowTitle("Win")
            self.msg_box.setText("You win!")
            self.msg_box.exec()

    def Exit(self):
        exit(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SudokuGame()

    window.show()
    app.exec()