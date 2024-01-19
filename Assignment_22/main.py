import sys
from functools import partial
from PySide6.QtWidgets import QMessageBox,QMainWindow,QApplication,QCheckBox,QLabel,QPushButton
from ui_main_window import Ui_MainWindow
from database import Database

class MainWindow(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui = Ui_MainWindow()
          self.ui.setupUi(self)
          self.db = Database()
          self.display_data()

     def clear_display(self):
          while self.ui.grid_Layout.count():
               item = self.ui.grid_Layout.takeAt(0)
               widget = item.widget()
               if widget:
                    widget.deleteLater()

     def display_data(self):
          self.clear_display()
          self.tasks = self.db.get_task()

          for i in range(len(self.tasks)):
               new_task_box = QCheckBox()
               new_label = QLabel()
               new_btn = QPushButton()

               new_btn.setText("💣")
               new_label.setText(self.tasks[i][1])
               self.ui.grid_Layout.addWidget(new_task_box, i, 0)
               self.ui.grid_Layout.addWidget(new_label, i, 1)
               self.ui.grid_Layout.addWidget(new_btn, i, 2)
               new_btn.clicked.connect(partial(self.db.remove_task, self.tasks[i][0]))

     def new_task(self):
          new_title = self.ui.title_text.text()
          new_description = self.ui.dec_text_box.toPlainText()
          feedback = self.db.add_new_task(new_title, new_description)
          if feedback == True:
               self.display_data()
               self.ui.title_text.setText("")
               self.ui.dec_text_box.setText("")
          else:
               message = QMessageBox()
               message.setText("Error")
               message.exec()

if __name__ == "__main__":
     app = QApplication(sys.argv)
     window = MainWindow()

     window.ui.btn_add_task.clicked.connect(partial(window.new_task))

     window.show()
     app.exec()
