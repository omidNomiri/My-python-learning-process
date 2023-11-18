import gtts

def load_database():
    global words_bank
    with open("Assignment_8/Translate.txt","r") as database_translate:
        temp = database_translate.read().split("\n")
        words_bank = []
        for line in range(0,len(temp) - 1,2):
            my_dictionary = {"english":temp[line],"persian":temp[line+1]}
            words_bank.append(my_dictionary)

def show_menu():
    print("1.translate english to persian")
    print("2.english text to speak")
    print("3.translate persian to english ")
    print("4.persian text to speak ")
    print("5.add a new word to database")
    print("6.exit")

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
    print("")

def english_text_to_speak():
    user_text = input("Please enter your english text: ")
    sound = gtts.gTTS(user_text,lang="en",slow=False)
    sound.save("Assignment_8/voice.mp3")

def translate_persian_to_english():
    user_text = input("Please enter your persian text: ")
    user_word = user_text.split(" ")
    
    for user_word in user_word:
        for word in words_bank:
            if user_word == word["persian"]:
                print(word["english"],end=" ")
                break
        else:
            print(user_word,end=" ")
    print("")

def persian_text_to_speak():
    user_text = input("Please enter your persian text: ")
    sound = gtts.gTTS(user_text,lang="ur",slow=False)
    sound.save("Assignment_8/voice.mp3")

def add_to_database():
    user_english_text = input("Please enter your English text: ")
    user_persian_text = input("Please enter your Persian text: ")
    with open("Assignment_8\Translate.txt", "a") as database:
        database.write(f"{user_english_text}\n{user_persian_text}\n")

load_database()

while True:
    show_menu()
    choice = int(input("what do yo want: "))

    if choice == 1:
        translate_english_to_persian()
    elif choice == 2:
        english_text_to_speak()
    elif choice == 3:
        translate_persian_to_english()
    elif choice == 4:
        persian_text_to_speak()
    elif choice == 5:
        add_to_database()
    elif choice == 6:
        print("Have a good day. \n Goodbye")
        exit(0)
