import sys
from random import randint
from sudoku import Sudoku
from functools import partial
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow ,QApplication ,QLineEdit ,QFileDialog
from ui_main_window import Ui_MainWindow

class Sudoku_game(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.mode = 0
          self.win = False

          self.ui.new_game_menu.triggered.connect(self.new_game)
          self.ui.open_file_menu.triggered.connect(self.open_file)
          self.ui.dark_mode_toggle_btn.clicked.connect(partial(self.theme_toggle))
          self.ui.dark_mode_toggle_btn.setText("🌑")
          self.line_text = [[None for row in range(9)] for column in range(9)]

          for row in range(9):
               for column in range(9):
                    new_line_edit = QLineEdit()
                    self.ui.grid_layout.addWidget(new_line_edit, row, column)
                    new_line_edit.setAlignment((PySide6.QtCore.Qt.AlignCenter))
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

     def theme_toggle(self):
          if self.mode == 0:
               self.ui.dark_mode_toggle_btn.setText("🌕")
               self.setStyleSheet("background-color: #404040; color: white;")
               self.mode = 1
          elif self.mode == 1:
               self.ui.dark_mode_toggle_btn.setText("🌑")
               self.setStyleSheet("")
               self.mode = 0

     def open_file(self):
          file_path = QFileDialog.getOpenFileName(self, 'Open file...')[0]

          with open(file_path, 'r') as text_file:
               text_file = open(file_path, 'r')
               text = text_file.read()
               rows = text.split('\n')
               puzzle_board = [[None for i in range(9)] for j in range(9)]
               for i in range(len(rows)):
                    cells = rows[i].split(' ')
                    for j in range(len(cells)):
                         puzzle_board[i][j] = int(cells[j])

               self.checkable = False
               for i in range(9):
                    for j in range(9):
                         if puzzle_board[i][j] != 0:
                              self.line_text[i][j].setText(str(puzzle_board[i][j]))
                              self.line_text[i][j].setReadOnly(True)
                         else:
                              self.line_text[i][j].setText('')
                              self.line_text[i][j].setReadOnly(False)
               self.checkable = True

     def validation(self, row, column ,text):
          if text not in ["1" ,"2" ,"3" ,"4" ,"5" ,"6" ,"7" ,"8" ,"9"]:
               self.line_text[row][column].setText("")

          self.check(self.line_text)

     def check(self ,board):
          for row in board:
               number_in_board = set()
               for number in row:
                    if number in number_in_board:
                         self.line_text[row][number].setStyleSheet("color:red;")
                         return False
                    number_in_board.add(number)
          
          for column in range(9):
               number_in_board = set()
               for row in board:
                    if row[column] in number_in_board:
                         self.line_text[number][column].setStyleSheet("color:red;")
                         return False
                    number_in_board.add(number)

          for row_start in range(0 ,9 ,3):
               for column_start in range(0 ,9 ,3):
                    number_in_box = set()
                    for row in range(row_start, row_start+3):
                         for col in range(column_start, column_start+3):
                              number = board[row][col]
                              if number in number_in_box:
                                   self.line_text[row][column].setStyleSheet("color:red;")
                                   return False
                              number_in_box.add(number)
          return True

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = Sudoku_game()

     window.show()
     app.exec()
