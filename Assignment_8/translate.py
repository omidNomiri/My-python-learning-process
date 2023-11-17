def load_database():
    global words_bank
    with open("Assignment_8\Translate.txt","r") as database_translate:
        temp = database_translate.read().split("\n")
        words_bank = []
        for line in range(0,len(temp),2):
            my_dictionary = {"english":temp[line],"persian":temp[line+1]}
            words_bank.append(my_dictionary)
    
load_database()
user_text = input("Please enter your english text: ")

user_word = user_text.split(" ")

for user_word in user_word:
    for word in words_bank:
        if user_word == word["english"]:
            print(word["persian"],end=" ")
            break
