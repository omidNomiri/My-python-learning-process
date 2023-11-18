import qrcode

PRODUCTS = []
factor = []

def read_database():
    with open("Assignment_7\database.txt", "r") as database:
        for line in database:
            line = line.strip()
            product_list = line.split(",")
            
            if len(product_list) == 4:
                my_dictionary = {"code": product_list[0], "name": product_list[1], "price": product_list[2], "storage": product_list[3]}
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
    print("7.QRcode product")
    print("8.Exit")

def add():
    code = int(input("Please enter your commodity id: "))
    name = str(input("Please enter your commodity name: "))
    price = int(input("Please enter your commodity price: "))
    storage = int(input("Please enter your commodity storage: "))
    new_product = {"code":code,"name":name,"price":price,"storage":storage}
    PRODUCTS.append(new_product)
    print("product add operation success.")

def edit():
    choice = int(input("you want change witch one?(1.name_2.price_3.storage): "))
    if choice == 1:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("select your product name: ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New name: ")
                row["name"] = new_product
        print("product edit operation success.")
    if choice == 2:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("select your product name: ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New price: ")
                row["price"] = new_product
        print("product edit operation success.")
    if choice == 3:
        for row in PRODUCTS:
            print(row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("select your product name: ")
        for row in PRODUCTS:
            if row["name"] == select:
                new_product = input("New storage: ")
                row["storage"] = new_product
        print("product edit operation success.")

def remove():
    global PRODUCTS
    code = int(input("Please enter your product id: "))
    new_products = [row for row in PRODUCTS if row['code'] != code]
    PRODUCTS = new_products
    print("Remove successful.")

def search():
    user_search = input("Please enter your product id or name: ")
    for product in PRODUCTS:
        if product["code"]==user_search or product["name"]==user_search:
            print(product["code"],"\t",product["name"],"\t",product["price"])
            break
    else:
        print("We dont have any product with this code or name.")

def show_list():
    for row in PRODUCTS:
        print(row["code"],"\t",row["name"],"\t",row["price"])

def buy():
    while True:
        for row in PRODUCTS:
            print(row["code"],"\t",row["name"],"\t",row["price"],"\t",row["storage"])
        select = input("Please enter your product code: ")
        for row in PRODUCTS:
            if select == row["code"]:
                user_count_buy = int(input("Please enter how much you want: "))
                if user_count_buy <= int(row["storage"]):
                    row["storage"] = int(row["storage"]) - user_count_buy
                    user_Basket = [row["name"],user_count_buy,row["price"]]
                    factor.append(user_Basket)
                    print("product buy operation success.")
                    break
                else:
                    print("We dont have a enough product for you!")
        else:
            print("We dont have any product with this code.")
        continue_shopping = input("Do you want to continue shopping? (y/n): ")
        if continue_shopping.lower() != "y":
            print_factor()
            break

def save_in_database():
    with open("Assignment_7\database.txt","w") as database:
        for row in PRODUCTS:
            code = row["code"]
            name = row["name"]
            price = row["price"]
            storage = row["storage"]
            data = str(f"{code},{name},{price},{storage}\n")
            database.write(data)

def print_factor():
    for row in factor:
        print(row)

def make_QRcode():
    product_code = int(input("Please enter your product code: "))
    for row in PRODUCTS:
        if product_code == int(row["code"]):
            code = row["code"]
            name = row["name"]
            price = row["price"]
            storage = row["storage"]
            product_info = f"{code},{name},{price},{storage}"
            qr_code = qrcode.make(product_info)
            qr_code.save("product-QRcode.png")
            print("product QRcode now available.")
    else:
        print("We dont have any product with this code.")

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
        make_QRcode()
    elif user_operation == 8:
        save_in_database()
        exit(0)
    else:
        print("enter number between 1 to 8.")
