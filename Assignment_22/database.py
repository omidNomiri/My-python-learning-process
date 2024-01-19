import sqlite3

class Database:
     def __init__(self):
          self.connection = sqlite3.connect("Assignment_22\\todolist.db")
          self.curser = self.connection.cursor()

     def get_task(self):
          query = "SELECT * FROM tb_tasks"
          result = self.curser.execute(query).fetchall()
          return result

     def add_new_task(self, new_task_title, new_task_description):
          query = f"INSERT INTO tb_tasks(title, description) VALUES ('{new_task_title}','{new_task_description}')"
          self.curser.execute(query)
          self.connection.commit()
          return True

     def remove_task(self, task_id):
          query = f"DELETE FROM tb_tasks WHERE id={task_id}"
          self.curser.execute(query)
          self.connection.commit()
          return True
