from media import Media

MOVIE_LIST = []

class Database:
    def __init__(self):
        ...
        
    def read(self):
        with open("Assignment_12\database.txt", "r") as database:
            for line in database:
                line = line.strip()
                movie_list = line.split(",")
            
                if len(movie_list) == 4:
                    my_object = Media(movie_list[0],movie_list[1],movie_list[2],movie_list[3])
                    MOVIE_LIST.append(my_object)

    def write(self):
        with open("Assignment_12\database.txt","w") as database:
            for row in MOVIE_LIST:
                data = f"{row[0]},{row[1]},{row[2]},{row[3]}\n"
                database.write(data)

