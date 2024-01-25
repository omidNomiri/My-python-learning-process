import sys
from random import randint
from sudoku import Sudoku
from functools import partial
from PySide6.QtWidgets import QMainWindow ,QApplication ,QLineEdit ,QFileDialog
from ui_main_window import Ui_MainWindow

class Sudoku_game(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.ui.new_game_menu.triggered.connect(self.new_game)
          self.ui.open_file_menu.triggered.connect(self.open_file)
          self.line_text = [[None for row in range(9)] for column in range(9)]

          for row in range(9):
               for column in range(9):
                    new_line_edit = QLineEdit()
                    self.ui.grid_layout.addWidget(new_line_edit, row, column)
                    new_line_edit.textChanged.connect(partial(self.validation ,row ,column))
                    self.line_text[row][column] = new_line_edit

          self.new_game()

     def new_game(self):
          puzzle = Sudoku(3, seed=randint(0, 1000)).difficulty(0.5)
          for row in range(9):
               for column in range(9):
                    if puzzle.board[row][column] != None:
                         self.line_text[row][column].setText(str(puzzle.board[row][column]))
                         self.line_text[row][column].setReadOnly(True)
                    else:
                         self.line_text[row][column].setText("")

     def open_file(self):
          file_path = QFileDialog.getOpenFileName(self ,"select your file")[0]

     def validation(self, row, column ,text):
          if text not in ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]:
               self.line_text[row][column].setText("")

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Sudoku_game()

     window.show()
     app.exec()
