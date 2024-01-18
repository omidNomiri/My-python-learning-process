import sqlite3

class Database:
     def __init__(self):
          self.connection = sqlite3.connect("Assignment_22\\todolist.db")
          self.curser = self.connection.cursor()

     def get_task(self):
          ...

     def add_new_task(self, new_task_title, new_task_description):
          ...
