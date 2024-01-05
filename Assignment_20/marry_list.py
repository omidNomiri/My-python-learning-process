import random

boys = ["Mohammad", "Alex", "Ali", "Kya", "Roan"]
girls = ["Lily", "Parry", "Mona", "Nazi", "Sima"]
marry_list = []

for boy in boys:
     girl = random.choice(girls)
     index = girls.index(girl)
     girls.pop(index)
     couple = girl + " and " + boy
     marry_list.append(couple)
     print(couple)
