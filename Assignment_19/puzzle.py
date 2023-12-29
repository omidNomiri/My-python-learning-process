import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = [
            [self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
            [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
            [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
            [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]
        ]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    game = Game()
    game.show()

    app.exec()
