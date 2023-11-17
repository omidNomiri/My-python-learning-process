PRODUCT = []

def read_database():
    with open("Assignment_7\database.txt","r") as database:
        for line in database:
            product_list = line.split(",")
            my_dictionary = {"code" : product_list[0],"name" : product_list[1],"price" : product_list[2],"storage" : product_list[3]}
            PRODUCT.append(my_dictionary)

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
    PRODUCT.append({"code":code,"name":name,"price":price,"storage":storage})

def edit():
    print("1.name")
    print("2.price")
    print("3.storage")
    choice = input("You want edit which field: ")
    if choice == 1:
        change_value = input("Enter your commodity name: ")
        PRODUCT.append(change_value[1])
    elif choice == 2:
        change_value = input("Enter your commodity price: ")
        PRODUCT.append(change_value[2])
    elif choice == 3:
        change_value = input("Enter your commodity storage: ")
        PRODUCT.append(change_value[3])

def remove():
    ...

def search():
    ...

def show_list():
    for row in PRODUCT:
        print(row)

def buy():
    ...


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
        with open("Assignment_7\database.txt","w") as database:
            for row in PRODUCT:
                database.write(str({"code":row["code"],"name":row["name"],"price":row["price"],"storage":row["storage"]})+"\n")
        exit(0)
