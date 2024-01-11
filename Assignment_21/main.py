import sqlite3

class Store:
     def __init__(self):
          self.data_base = sqlite3.connect("store_database.db")
          self.curser = self.data_base.cursor()
          self.show_action_list = "WELCOME TO STORE\n 1. ADD item \n 2. EDIT item \n 3. Remove \n 4. Search \n 5. Show list of item \n 6. Buy \n 7. Exit"

     def Add_item(self):
          product_name = str(input("name of item: "))
          product_price = float(input("price of item: "))
          product_count = int(input("how much you have: "))
          self.data_base.execute(f"INSERT INTO Products(name, price, storage) VALUES({product_name},{product_price},{product_count})")

     def edit_item(self):
          ...

     def remove_item(self):
          ...

     def search_item(self):
          ...

     def show_list_item(self):
          ...

     def buy(self):
          ...

app = Store()

while True:
     print(app.show_action_list)
