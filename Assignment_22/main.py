import sys
from functools import partial
from PySide6.QtWidgets import QMessageBox,QMainWindow,QApplication,QCheckBox,QLabel,QPushButton
from PySide6.QtGui import QFont
from ui_main_window import Ui_TODOAPP
from database import Database

class MainWindow(QMainWindow):
     def __init__(self):
          super().__init__()
          self.ui = Ui_TODOAPP()
          self.ui.setupUi(self)
          self.db = Database()
          self.display_data()
          self.priority = 0

     def display_data(self):
          tasks_done = []
          tasks_not_done = []
          sort_tasks = []
          self.repaint()
          self.tasks = self.db.get_task()
          for task in self.tasks:
               if task[3] == 1:
                    tasks_done.append(list(task))
               else:
                    tasks_not_done.append(list(task))

          tasks_not_done.sort(key=lambda task: task[4], reverse=True)
          sort_tasks += (tasks_not_done + tasks_done)

          for i in range(len(sort_tasks)):
               task_box = QCheckBox()
               label = QLabel()
               remove_btn = QPushButton()
               detail_btn = QPushButton()

               remove_btn.setText("💣")
               remove_btn.setMaximumHeight(26)
               detail_btn.setText("!")
               detail_btn.setMaximumHeight(26)
               label.setFont(QFont("Arial", 16))
               label.setText(sort_tasks[i][1])
               if sort_tasks[i][3] == 1:
                    task_box.setChecked(True)
                    label.setStyleSheet("border-radius: 6px;  background-color: #ff5050;")
                    remove_btn.setStyleSheet("border-radius: 6px;  background-color: #ff5050;")
                    detail_btn.setStyleSheet("border-radius: 6px;  background-color: #ff5050;")
               elif sort_tasks[i][3] == 0:
                    label.setStyleSheet("border-radius: 6px;  background-color: #33cc33;")
                    remove_btn.setStyleSheet("border-radius: 6px;  background-color: #33cc33;")
                    detail_btn.setStyleSheet("border-radius: 6px;  background-color: #33cc33;")
               self.ui.grid_Layout.addWidget(task_box, i, 0)
               task_box.clicked.connect(partial(self.db.done_task, sort_tasks[i][0], sort_tasks[i][3]))
               if sort_tasks[i][4] == 3:
                    label.setStyleSheet("color:Red;")
               elif sort_tasks[i][4] == 2:
                    label.setStyleSheet("color:#ff6600;")
               elif sort_tasks[i][4] == 1:
                    label.setStyleSheet("color:#3366ff;")
               elif sort_tasks[i][4] == 0:
                    label.setStyleSheet("color:#33cc33;")
               self.ui.grid_Layout.addWidget(label, i, 1)
               self.ui.grid_Layout.addWidget(remove_btn, i, 2)
               remove_btn.clicked.connect(partial(self.db.remove_task, sort_tasks[i][0]))
               self.ui.grid_Layout.addWidget(detail_btn, i, 3)
               detail_btn.clicked.connect(partial(self.show_detail, sort_tasks[i]))

     def set_task_priority(self, priority):
          self.priority = priority

     def new_task(self):
          new_title = self.ui.title_text.text()
          new_description = self.ui.dec_text_box.toPlainText()
          date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
          time = self.ui.timeEdit.time().toString()
          feedback = self.db.add_new_task(new_title, new_description, self.priority, date, time)
          if feedback == True:
               self.display_data()
               self.ui.title_text.setText("")
               self.ui.dec_text_box.setText("")
          else:
               message = QMessageBox()
               message.setText("Error")
               message.exec()
          self.repaint()

     def show_detail(self,task_info):
          if task_info[3] == 0:
               is_done = False
          if task_info[3] == 1:
               is_done = True
          message = QMessageBox()
          message.setWindowTitle("Task information")
          message.setText(f"task title: {task_info[1]} \ndescribe: {task_info[2]} \ndata: {task_info[5]} \ntime: {task_info[6]} \nstatus task: {is_done}")
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
