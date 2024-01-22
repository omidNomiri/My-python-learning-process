import sqlite3

class Database:
     def __init__(self):
          self.connection = sqlite3.connect("Assignment_22\\tasks.db")
          self.curser = self.connection.cursor()

     def get_task(self):
          try:
               query = "SELECT * FROM tb_tasks"
               result = self.curser.execute(query).fetchall()
               return result
          except Exception as error:
               print(f"get task from database func error: {error}")

     def add_new_task(self, new_task_title, new_task_description, priority, date, time):
          try:
               query = f"INSERT INTO tb_tasks(title, description, priority, date, time) VALUES ('{new_task_title}','{new_task_description}','{priority}','{date}','{time}')"
               self.curser.execute(query)
               self.connection.commit()
               return True
          except Exception as error:
               print(f"add new task func error: {error}")

     def remove_task(self, task_id):
          try:
               query = f"DELETE FROM tb_tasks WHERE id={task_id}"
               self.curser.execute(query)
               self.connection.commit()
               return True
          except Exception as error:
               print(f"delete task func error: {error}")

     def done_task(self, task_id, is_done):
          try:
               if is_done == 0:
                    query = f"UPDATE tb_tasks SET is_done=1 WHERE id={task_id} AND is_done=0"
               else:
                    query = f"UPDATE tb_tasks SET is_done=0 WHERE id={task_id} AND is_done=1"
               self.curser.execute(query)
               self.connection.commit()
               return True
          except Exception as error:
               print(f"done task func error: {error}")
