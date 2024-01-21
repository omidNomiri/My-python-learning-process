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
          self.priority = 0

     def clear_display(self):
          while self.ui.grid_Layout.count():
               item = self.ui.grid_Layout.takeAt(0)
               widget = item.widget()
               if widget:
                    widget.deleteLater()

     def display_data(self):
          tasks_done = []
          tasks_not_done = []
          sort_tasks = []
          self.clear_display()
          self.tasks = self.db.get_task()
          for task in self.tasks:
               if task[3] == 1:
                    tasks_done.append(list(task))
               else:
                    tasks_not_done.append(list(task))

          tasks_not_done.sort(key=lambda task: task[4], reverse=True)
          sort_tasks += (tasks_not_done + tasks_done)

          for i in range(len(sort_tasks)):
               print(sort_tasks)
               new_task_box = QCheckBox()
               new_label = QLabel()
               new_btn = QPushButton()

               new_btn.setText("💣")
               new_label.setText(sort_tasks[i][1])
               if sort_tasks[i][3] == 1:
                    new_task_box.setChecked(True)
               self.ui.grid_Layout.addWidget(new_task_box, i, 0)
               new_task_box.clicked.connect(partial(self.db.done_task, sort_tasks[i][0], sort_tasks[i][3]))
               self.ui.grid_Layout.addWidget(new_label, i, 1)
               self.ui.grid_Layout.addWidget(new_btn, i, 2)
               new_btn.clicked.connect(partial(self.db.remove_task, sort_tasks[i][0]))

     def set_task_priority(self, priority):
          self.priority = priority

     def new_task(self):
          new_title = self.ui.title_text.text()
          new_description = self.ui.dec_text_box.toPlainText()
          feedback = self.db.add_new_task(new_title, new_description, self.priority)
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
     window.ui.rd_imp_qui.clicked.connect(partial(window.set_task_priority, 3))
     window.ui.rd_imp_not_qui.clicked.connect(partial(window.set_task_priority, 2))
     window.ui.rd_not_imp_qui.clicked.connect(partial(window.set_task_priority, 1))
     window.ui.rd_not_imp_not_qui.clicked.connect(partial(window.set_task_priority, 0))

     window.show()
     app.exec()
