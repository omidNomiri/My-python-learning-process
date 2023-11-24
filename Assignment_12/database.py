from media import Media
from series import Series

MOVIE_LIST = []

class Database:
    def __init__(self):
        ...

    @staticmethod
    def read():
        with open("Assignment_12\database.txt", "r") as database:
            for line in database:
                line = line.strip()
                movie_list = line.split(",")
                
                actors = movie_list[5].strip('][').split(',')
                genres = movie_list[6].strip('][').split(',')

                if len(movie_list) > 8:
                    my_object = Series(movie_list[0],movie_list[1],movie_list[2],movie_list[3],movie_list[4],actors,genres,movie_list[7],movie_list[8])

                else:
                    my_object = Media(movie_list[0],movie_list[1],movie_list[2],movie_list[3],movie_list[4],actors,genres,movie_list[7])

                MOVIE_LIST.append(my_object)

    def write(self):
        with open("Assignment_12\database.txt","w") as database:
            for row in MOVIE_LIST:
                data = f"{row[0]},{row[1]},{row[2]},{row[3]}\n"
                database.write(data)
