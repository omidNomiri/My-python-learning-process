import sqlite3

class Database ():

    def __init__(self):
        self.con = sqlite3.connect("Assignment_25/alarm.db")
        self.cur = self.con.cursor()

    def get_alarms(self):
        query = f"SELECT * FROM alarms"
        result = self.cur.execute(query)
        tasks = result.fetchall()
        return (tasks)

    def add_alarm(self, time, title):
        try:
            query = f"INSERT INTO alarms (time, title) VALUES ('{time}','{title}')"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def delete_alarm(self, id):
        try:
            query = f"DELETE FROM alarms WHERE id = {id}"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False

    def update_alarm(self, id, mode):
        try:
            query = f"UPDATE alarms SET mode = {mode} WHERE id = {id}"
            self.cur.execute(query)
            self.con.commit()
            return True
        except:
            return False
