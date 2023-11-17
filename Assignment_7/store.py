PRODUCTS = []

def read_database():
    with open("Assignment_7\database.txt","r") as database:
        for line in database:
            product_list = line.split(",")
            my_dictionary = {"code" : product_list[0],"name" : product_list[1],"price" : product_list[2],"storage" : product_list[3]}
            PRODUCTS.append(my_dictionary)

print("Loading.....")
read_database()
print("loading is completed!")

def show_menu():
    print("1.Add")
    print("2.Edit")
    print("3.Remove")
    print("4.Search")
    print("5.Show list")
    print("6.Buy")
    print("7.Exit")

def add():
    code = int(input("Please enter your commodity id: "))
    name = str(input("Please enter your commodity name: "))
    price = int(input("Please enter your commodity price: "))
    storage = int(input("Please enter your commodity storage: "))
    new_product = {"code":code,"name":name,"price":price,"storage":storage}
    PRODUCTS.append(new_product)

def edit():
    ...

def remove():
    code = int(input("Please enter your product id: "))
    PRODUCTS = [row for row in PRODUCTS if row['code'] != code]
    print("Remove successful.")

def search():
    user_search = input("Please enter your product id or name: ")
    for product in PRODUCTS:
        if product["code"]==user_search or product["name"]:
            print(product["code"],"\t",product["name"],"\t",product["price"])
            break
    else:
        print("not find.")

def show_list():
    for row in PRODUCTS:
        print(row["code"],"\t",row["name"],"\t",row["price"])

def buy():
    ...

def save_in_database():
    with open("Assignment_7\database.txt","a") as database:
        for row in PRODUCTS:
            code = row["code"]
            name = row["name"]
            price = row["price"]
            storage = row["storage"]
            data = str(f"{code},{name},{price},{storage}")
            database.write(data)

while True:
    show_menu()
    user_operation = int(input("Please enter you want: "))
    if user_operation == 1:
        add()
    elif user_operation == 2:
        edit()
    elif user_operation == 3:
        remove()
    elif user_operation == 4:
        search()
    elif user_operation == 5:
        show_list()
    elif user_operation == 6:
        buy()
    elif user_operation == 7:
        save_in_database()
        exit(0)
    else:
        print("enter number between 1 to 7.")