import sys
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
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
          while self.ui.form_Layout.count():
            item = self.ui.form_Layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

     def display_data(self):
          self.clear_display()
          self.tasks = self.db.get_task()

          for i in range(len(self.tasks)):
               new_task_box = QCheckBox()
               new_label = QLabel()
               new_label.setText(self.tasks[i][1])

               self.ui.form_Layout.addWidget(new_task_box)
               self.ui.form_Layout.addWidget(new_label)

     def new_task(self):
          new_title = self.ui.title_text.text()
          new_description = self.ui.dec_text_box.toPlainText()
          feedback = self.db.add_new_task(new_title, new_description)
          if feedback == True:
               self.display_data()
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
