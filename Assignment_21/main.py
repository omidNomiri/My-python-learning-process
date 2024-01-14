import sqlite3

class Store:
     def __init__(self):
          self.data_base = sqlite3.connect("Assignment_21\store_database.db")
          self.curser = self.data_base.cursor()
          self.show_action_list = "WELCOME TO STORE\n 1. ADD item \n 2. EDIT item \n 3. Remove \n 4. Search \n 5. Show list of item \n 6. Buy \n 7. Exit"

     def add_item(self):
          product_name = str(input("name of item: "))
          product_price = float(input("price of item: "))
          product_count = int(input("how much you have: "))
          self.curser.execute("INSERT INTO Products(name, price, storage) VALUES (?, ?, ?)", (product_name, product_price, product_count))
          self.data_base.commit()

     def edit_item(self):
          self.show_item_list()
          target_item_id = int(input("please enter your product id: "))
          edit_target = int(input("what you want edit \n 1.name\n 2.price\n 3.storage\nyour choice: "))
          if edit_target in (1,2,3):
               new_value = input("please enter your new value: ")
               if edit_target == 1:
                    self.curser.execute("UPDATE Products SET name=? where id=?",(new_value, target_item_id))
               elif edit_target == 2:
                    self.curser.execute("UPDATE Products SET price=? where id=?", (new_value, target_item_id))
               elif edit_target == 3:
                    self.curser.execute("UPDATE Products SET storage=? where id=?", (new_value, target_item_id))
               self.data_base.commit()

     def remove_item(self):
          self.show_item_list()
          target_item_id = input("please enter your product id: ")
          self.curser.execute("DELETE FROM Products WHERE id=?", (target_item_id))
          self.data_base.commit()

     def search_item(self):
          target_item_id = input("Please enter your product name or product id: ")
          items = self.curser.execute("SELECT * FROM Products WHERE id=? OR name=?", (target_item_id,target_item_id)).fetchall()
          for item in items:
               print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Storage: {item[3]}")

     def show_item_list(self):
          items = self.curser.execute("SELECT * FROM Products").fetchall()
          for item in items:
               print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Storage: {item[3]}")

     def buy(self):
          ...

app = Store()

while True:
     print(app.show_action_list)
     choice = int(input("what do you want: "))

     if choice == 1:
          app.add_item()
     elif choice == 2:
          app.edit_item()
     elif choice == 3:
          app.remove_item()
     elif choice == 4:
          app.search_item()
     elif choice == 5:
          app.show_item_list()
     elif choice == 6:
          app.buy()
     elif choice == 7:
          exit(0)
