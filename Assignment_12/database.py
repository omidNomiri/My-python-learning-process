from media import Media
from series import Series
import re

MOVIE_LIST = []

class Database:
    def __init__(self):
        ...

    @staticmethod
    def read():
        with open("Assignment_12\database.txt", "r") as database:
            for line in database:
                line = line.strip()
                pattern = r",(?![^\[\]]*\])"
                movie_list = re.split(pattern, line)

                if len(movie_list) > 8:
                    data = Series(movie_list[0],movie_list[1],movie_list[2],movie_list[3],movie_list[4],movie_list[5],movie_list[6],movie_list[7],movie_list[8])
                else:
                    data = Media(movie_list[0],movie_list[1],movie_list[2],movie_list[3],movie_list[4],movie_list[5],movie_list[6],movie_list[7])

                MOVIE_LIST.append(data)

    @staticmethod
    def write():
        with open("Assignment_12\database.txt","w") as database:
            for row in MOVIE_LIST:
                if isinstance(row,Series):
                    data = f"{row.name},{row.director},{row.IMDB_score},{row.url},{row.duration},{row.actor},{row.genre},{row.release_year},{row.episode}\n"
                else:
                    data = f"{row.name},{row.director},{row.IMDB_score},{row.url},{row.duration},{row.actor},{row.genre},{row.release_year}\n"
                database.write(data)
