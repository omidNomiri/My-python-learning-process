import sqlite3

class Store:
     def __init__(self):
          self.data_base = sqlite3.connect("Assignment_21\store_database.db")
          self.curser = self.data_base.cursor()
          self.show_action_list = "WELCOME TO STORE\n 1. ADD item \n 2. EDIT item \n 3. Remove \n 4. Search \n 5. Show list of item \n 6. Buy \n 7. Exit"
          self.factor = []

     def add_item(self):
          try:
               product_name = str(input("name of item: "))
               product_price = float(input("price of item: "))
               product_count = int(input("how much you have: "))

               self.curser.execute("INSERT INTO Products(name, price, storage) VALUES (?, ?, ?)", (product_name, product_price, product_count))
               self.data_base.commit()

               print("item adding successfully")
          except Exception as error:
               print(f"add item error: {error}")

     def edit_item(self):
          try:
               self.show_item_list()
               target_item_id = int(input("please enter your product id: "))
               edit_target = int(input("what you want edit \n 1.name\n 2.price\n 3.storage\nyour choice: "))
               
               if edit_target in (1,2,3):
                    new_value = input("please enter your new value: ")
                    if edit_target == 1:
                         self.curser.execute("UPDATE Products SET name=? Where id=?",(new_value, target_item_id))
                    elif edit_target == 2:
                         self.curser.execute("UPDATE Products SET price=? Where id=?", (new_value, target_item_id))
                    elif edit_target == 3:
                         self.curser.execute("UPDATE Products SET storage=? Where id=?", (new_value, target_item_id))
                    
                    self.data_base.commit()
                    print("Edit item successfully")
               else:
                    print("Invalid choice.")
          except Exception as error:
               print(f"Edit item error: {error}")

     def remove_item(self):
          try:
               self.show_item_list()
               target_item_id = input("please enter your product id: ")

               self.curser.execute("DELETE FROM Products WHERE id=?", (target_item_id))
               self.data_base.commit()
               print("Item removed successfully")
          except Exception as error:
               print(f"remove item error: {error}")

     def search_item(self):
          try:
               target_item_id = input("Please enter your product name or product id: ")
               items = self.curser.execute("SELECT * FROM Products WHERE id=? OR name=?", (target_item_id,target_item_id)).fetchall()

               for item in items:
                    print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Storage: {item[3]}")
          except Exception as e:
               print(f"Error in searching: {e}")

     def show_item_list(self):
          try:
               items = self.curser.execute("SELECT * FROM Products").fetchall()

               for item in items:
                    print(f"ID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Storage: {item[3]}")
          except Exception as e:
               print(f"Error in displaying: {e}")

     def buy(self):
          try:
               while True:
                    self.show_item_list()
                    item_customer_want = input("Please enter your product name or product id: ")
                    how_many_item = int(input("How many: "))
                    self.curser.execute("UPDATE Products SET storage= storage - ? WHERE id=? OR name=?", (how_many_item, item_customer_want, item_customer_want))
                    item = self.curser.execute("SELECT * FROM Products WHERE id=? OR name=?", (item_customer_want, item_customer_want)).fetchall()

                    if item:
                         item = item[0]
                         list_for_factor = [str(value) for value in item]
                         self.factor.append(list_for_factor)
                         self.data_base.commit()
                         print("Item successfully add in your basket")

                         continue_shopping = input("Do you want to continue shopping? (y/n): ")
                         if continue_shopping.lower() != "y":
                              for item in self.factor:
                                   print(item)
                              break
                    else:
                         print("Item not found")
                         break
          except Exception as e:
               print(f"Error in buy item: {e}")

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
