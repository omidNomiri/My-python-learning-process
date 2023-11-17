def load_database():
    global words_bank
    with open("Assignment_8\Translate.txt","r") as database_translate:
        temp = database_translate.read().split("\n")
        words_bank = []
        for line in range(0,len(temp),2):
            my_dictionary = {"english":temp[line],"persian":temp[line+1]}
            words_bank.append(my_dictionary)

def translate_english_to_persian():
    user_text = input("Please enter your english text: ")
    user_word = user_text.split(" ")
    
    for user_word in user_word:
        for word in words_bank:
            if user_word == word["english"]:
                print(word["persian"],end=" ")
                break
        else:
            print(user_word,end=" ")

def show_menu():
    print("1.translate english to persian")
    print("2.translate persian to english ")
    print("3.add a new word to database")
    print("4.exit")

load_database()

while True:
    show_menu()
    choice = int(input("what do yo want: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        ...
    elif choice == 3:
        ...
    elif choice == 4:
        print("Have a good day. \n Goodbye")
